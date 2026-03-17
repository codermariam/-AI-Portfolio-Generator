from github import Github
from github.GithubException import GithubException

def deploy_to_github(pat, repo_name, readme_content, html_content):
    try:
        # Authenticate
        g = Github(pat)
        user = g.get_user()
        
        # Check if repo exists, if not create it
        try:
            repo = user.get_repo(repo_name)
            repo_exists = True
        except GithubException as e:
            if e.status == 404:
                # Repo not found, let's create it
                repo = user.create_repo(
                    name=repo_name,
                    description="My AI-generated portfolio",
                    private=False,
                    auto_init=True  # Important to initialize so we have a main branch
                )
                repo_exists = False
            else:
                return False, f"GitHub Error checking repo: {e.data.get('message', str(e))}"

        # Get default branch (usually main or master)
        default_branch = repo.default_branch

        # Determine if we need to update or create README.md
        try:
            readme_file = repo.get_contents("README.md", ref=default_branch)
            repo.update_file("README.md", "Update AI-generated README", readme_content, readme_file.sha, branch=default_branch)
        except GithubException as e:
            if e.status == 404:
                repo.create_file("README.md", "Add AI-generated README", readme_content, branch=default_branch)
            else:
                return False, f"Failed updating README.md: {e.data.get('message', str(e))}"

        # Determine if we need to update or create index.html
        try:
            html_file = repo.get_contents("index.html", ref=default_branch)
            repo.update_file("index.html", "Update AI-generated index.html", html_content, html_file.sha, branch=default_branch)
        except GithubException as e:
            if e.status == 404:
                repo.create_file("index.html", "Add AI-generated index.html", html_content, branch=default_branch)
            else:
                return False, f"Failed updating index.html: {e.data.get('message', str(e))}"
        
        url = f"https://{user.login}.github.io/{repo_name}/"
        success_msg = f"Deployment successful! Repository: https://github.com/{user.login}/{repo_name}\n\n"
        success_msg += "To see the live page, make sure GitHub Pages is enabled in your repository settings pointing to the `main` or `master` branch."
        
        return True, success_msg

    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"
