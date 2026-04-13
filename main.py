from src.triage_system import BugTriageSystem

if __name__ == "__main__":
    system = BugTriageSystem()
    
    # Test triage
    test_bug = "Login page crashes when user resets password"
    result = system.triage(test_bug)
    print(result)
