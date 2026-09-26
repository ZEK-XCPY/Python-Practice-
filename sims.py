# Basic Intelligent Agent: Vacuum Cleaner Agent

 

class VacuumEnvironment:

    """

    Represents the environment in which the intelligent agent operates.

    The environment contains two rooms: A and B.

    """

 

    def __init__(self, room_a="Dirty", room_b="Dirty", start_location="A"):

        # Environmental conditions

        self.rooms = {

            "A": room_a,

            "B": room_b

        }

 

        # Initial position of the agent

        self.agent_location = start_location

 

    def get_percept(self):

        """

        Returns the information currently perceived by the agent.

        """

 

        current_status = self.rooms[self.agent_location]

 

        return {

            "location": self.agent_location,

            "status": current_status

        }

 

    def execute_action(self, action):

        """

        Updates the environment according to the agent's action.

        """

 

        reward = 0

 

        if action == "CLEAN":

            if self.rooms[self.agent_location] == "Dirty":

                self.rooms[self.agent_location] = "Clean"

                reward = 10

            else:

                reward = -1

 

        elif action == "MOVE_RIGHT":

            if self.agent_location == "A":

                self.agent_location = "B"

                reward = -1

 

        elif action == "MOVE_LEFT":

            if self.agent_location == "B":

                self.agent_location = "A"

                reward = -1

 

        return reward

 

    def goal_reached(self):

        """

        Checks whether all rooms are clean.

        """

 

        return self.rooms["A"] == "Clean" and self.rooms["B"] == "Clean"

 

    def display_environment(self):

        """

        Displays the current environmental conditions.

        """

 

        print(

            f"Room A: {self.rooms['A']} | "

            f"Room B: {self.rooms['B']} | "

            f"Agent Location: {self.agent_location}"

        )

 

 

class SimpleReflexAgent:

    """

    An intelligent agent that makes decisions using condition-action rules.

    """

 

    def __init__(self):

        self.performance_score = 0

 

    def decide_action(self, percept):

        """

        Selects an action based on the current percept.

        """

 

        location = percept["location"]

        status = percept["status"]

 

        # Rule 1

        if status == "Dirty":

            return "CLEAN"

 

        # Rule 2

        elif location == "A":

            return "MOVE_RIGHT"

 

        # Rule 3

        elif location == "B":

            return "MOVE_LEFT"

 

        return "NO_ACTION"

 

 

def run_simulation(environment, agent, maximum_steps=10):

    """

    Runs the intelligent agent in the environment.

    """

 

    print("Initial Environment")

    environment.display_environment()

    print("-" * 60)

 

    if environment.goal_reached():

        print("Both rooms are already clean.")

        return

 

    for step in range(1, maximum_steps + 1):

 

        # Agent receives percept from the environment

        percept = environment.get_percept()

 

        # Agent makes a decision

        action = agent.decide_action(percept)

 

        # Environment executes the selected action

        reward = environment.execute_action(action)

 

        # Update the agent's performance

        agent.performance_score += reward

 

        print(f"Step {step}")

        print(f"Percept received : {percept}")

        print(f"Action selected  : {action}")

        print(f"Reward received  : {reward}")

 

        environment.display_environment()

        print("-" * 60)

 

        # Stop when all rooms become clean

        if environment.goal_reached():

            print("Goal achieved: Both rooms are clean.")

            break

 

    print(f"Final performance score: {agent.performance_score}")

 

 

# ---------------------------------------------------

# Create the environment and intelligent agent

# ---------------------------------------------------

 

environment = VacuumEnvironment(

    room_a="Dirty",

    room_b="Dirty",

    start_location="A"

)

 

agent = SimpleReflexAgent()

 

# Start the simulation

run_simulation(environment, agent)
