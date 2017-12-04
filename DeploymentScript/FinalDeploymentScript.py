from EnvironmentSetup import env_setup
from IntializeInstances import initialize_instances
from TerminationScript import terminate_instances

if __name__ == "__main__":
    """1. Initialize AWS Instances
       2. Setup Instance environment with all necessary dependencies
       3. Terminate instance
        IMPORTANT! Must make appropriate changes to InitializeInstances.py
                    and EnvironmentSetup.py TerminationScript.py"""
    initialize_instances();
    env_setup();
    terminate_instances();
