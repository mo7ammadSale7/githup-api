from django.http import JsonResponse
import requests


def git_data_form_github(request):
    date = "2021-06-29"
    per_page = 100
    repos_url = f'https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&page=1&per_page={per_page}'
    repos_results = requests.get(repos_url).json()
    language = []
    for repo in repos_results["items"]:
        language_url = f'https://api.github.com/search/repositories?q=language:{repo["language"]}&sort=forks&order=desc'
        language_results = requests.get(language_url).json()
        language.append(
            {
                'name': repo["language"],
                'num_of_repos': language_results["total_count"],
                'list_of_repos': language_results['items'],
            })

    return JsonResponse(language, safe=False)
