import os
from crewai import Agent, Task, Crew, LLM
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

llm = LLM(model="qwen/qwen3.5-122b-a10b", api_key=api_key, base_url="https://integrate.api.nvidia.com/v1")

class TripAgents:
    def __init__(self):
        self.llm = llm
    
    def city_selector_agent(self):
        return Agent(
            role = "You are a city selection expert.",
            goal = "Identify the best cities to visit based on user preferences.",
            backstory = "You have extensive knowledge of global cities, their attractions, culture, and travel logistics.",
            llm = self.llm,
            verbose = True
        )
        
    def local_expert_agent(self):
        return Agent(
            role = "You are a local travel expert.",
            goal = "Provide detailed information about local attractions, dining, and cultural experiences.",
            backstory = "You have lived in various cities around the world and have insider knowledge of the best places to visit.",
            llm = self.llm,
            verbose = True
        )
        
    def travel_planner_agent(self):
        return Agent(
            role = "You are a travel planning expert.",
            goal = "Create detailed travel itineraries based on user preferences and constraints.",
            backstory = "You have experience in planning trips for various types of travelers, ensuring a balance of activities, relaxation, and cultural experiences.",
            llm = self.llm,
            verbose = True
        )
        
    def budget_manager_agent(self):
        return Agent(
            role = "You are a budget management expert.",
            goal = "Help users manage their travel budgets effectively, providing cost-saving tips and budget-friendly options.",
            backstory = "You have a background in finance and travel, allowing you to offer practical advice on how to maximize travel experiences without overspending.",
            llm = self.llm,
            verbose = True
        )        

class TripTasks:
    def __init__(self):
        pass
    
    def city_selection_task(self, agent, inputs):
        return Task(
            name = "City Selection Task",
            description = (
                f"Analyze the user's preferences and select the best cities to visit.\n"
                f"-Travel Type: {inputs['travel_type']}\n"
                f"-Interests: {inputs['interests']}\n"
                f"-Season: {inputs['season']}\n"
                "Output: Provide 3 recommended cities with a brief explanation for each."
            ),
            agent = agent,
            expected_output = "Bullet point list of 3 cities with a 2 line explanation of each"  
        )
        
    def city_research_task(self, agent, city):
        return Task(
            name = "City Research Task",
            description = (
                f"Research the city '{city}' and provide detailed information about its attractions, dining options, cultural experiences,travel logistics and accommodation.\n"
                "Output: Provide a comprehensive overview of the city, including must-visit places, local cuisine recommendations, cultural insights, practical travel tips and accommodation options."
            ),
            agent = agent,
            expected_output = "Organised sections with clear headings and bullet points."
        )
        
    def itinerary_creation_task(self, agent, inputs, cities):
        return Task(
            name = "Itinerary Creation Task",
            description = (
                f"Create a {inputs['duration']}-day travel itinerary for the selected cities: {', '.join(cities)}.\n"
                "-Daily schedule with time allocations for each activity.\n"
                "-Activity sequencing to optimize travel time and experience.\n"
                "-Transportation between locations\n"
                "-Meal planning and dining recommendations\n"
            ),
            agent = agent,
            expected_output = "Day-by-day Table format itinerary with time slots and activity details"
        )
        
    def budget_planning_task(self, agent, inputs, itinerary):
        return Task(
            name = "Budget Planning Task",
            description = (
                f"Analyze the provided itinerary and create a detailed budget plan for selected budget range ({inputs['budget']}) for the trip covering:\n"
                "-Cost estimates for transportation, accommodation, meals and activities.\n"
                "-Suggestions for cost-saving measures and budget-friendly alternatives.\n"
                "-Overall budget summary with breakdowns by category."
            ),
            agent = agent,
            context = [itinerary],
            expected_output = "Detailed budget table with cost breakdowns and savings suggestions"
        )

class TripTools:

    def __init__(self, inputs):
        self.inputs = inputs

    def run_trip_planner(self):

        # Create Agents
        city_selector_agent = TripAgents().city_selector_agent()
        local_expert_agent = TripAgents().local_expert_agent()
        travel_planner_agent = TripAgents().travel_planner_agent()
        budget_manager_agent = TripAgents().budget_manager_agent()

        # Create Tasks
        select_cities = TripTasks().city_selection_task(
            city_selector_agent,
            self.inputs
        )

        research_city = TripTasks().city_research_task(
            local_expert_agent,
            "Mumbai"  
        )

        create_itinerary = TripTasks().itinerary_creation_task(
            travel_planner_agent,
            self.inputs,
            ["Mumbai"]
        )  

        plan_budget = TripTasks().budget_planning_task(
            budget_manager_agent,
            self.inputs,
            create_itinerary
        )

        # Create Crew
        crew = Crew(
            agents=[
                city_selector_agent,
                local_expert_agent,
                travel_planner_agent,
                budget_manager_agent
            ],
            tasks=[
                select_cities,
                research_city,
                create_itinerary,
                plan_budget
            ],
            verbose=True
        )

        # Run Crew
        result = crew.kickoff()

        # Process Outputs
        final_result = {}

        if hasattr(result, "tasks_output"):

            tasks_list = result.tasks_output

            final_result = {
                "city_selection": (
                    tasks_list[0].raw
                    if len(tasks_list) > 0
                    else ""
                ),

                "city_research": (
                    tasks_list[1].raw
                    if len(tasks_list) > 1
                    else ""
                ),

                "itinerary_creation": (
                    tasks_list[2].raw
                    if len(tasks_list) > 2
                    else ""
                ),

                "budget_planning": (
                    tasks_list[3].raw
                    if len(tasks_list) > 3
                    else ""
                )
            }

        else:
            print("Crew Result:", result)

        return final_result