from jira import JIRA

from JIRA.constants import JIRA_BUZZTIME_DOMAIN


def get_open_tasks(jira_username, jira_password):
    """
    Get the open tasks from the jira username passed
    :param jira_username: A valid JIRA username
    :return: A list of open tasks
    """

    authed_jira = JIRA(JIRA_BUZZTIME_DOMAIN, basic_auth=(jira_username, jira_password))
    issues = authed_jira.search_issues('assignee='+jira_username+' AND status in  ("Open" ,"In Progress" )')

    return issues


