from JIRA.controller import get_open_tasks
import getpass


def main():
    print("Hello. Welcome to Tracktive.")
    print("Please Enter your JIRA credentials\n")
    jira_username = raw_input("username: ")
    jira_password = getpass.getpass("password: ")
    open_tasks = get_open_tasks(jira_username, jira_password)

    print("Your open tasks are:\n")
    for task in open_tasks:
        print(task.key + ": " + task.fields.summary)



if __name__ == "__main__":
    main()
