from django.shortcuts import render, redirect
import requests
# Create your views here.

def doggy_list(request):
    return render(request, "doggy_list.html")

def doggy_api(request):
    base_url = 'https://dog.ceo/api/breed/'
    selection = request.POST['dog_selection']
    URL = base_url + selection + '/images/random'

    '''
    URL 연결이 잘 되었는지 확인하기 위해 print()를 사용하여 출력 해 봅니다. 
    print(URL)
    '''

    response = requests.get(URL)

    '''
    request로 올바른 상태값인 200이 나오는지 확인하고 우리가 적어준 요청대로 응답했는지 확인합니다.
    print(response.status_code)
    print(response.text)
    '''
    

    response_dictionary = response.json()
    dog = response_dictionary['message']

    return render(request, 'doggy_api.html', {'dog':dog})
