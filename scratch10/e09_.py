from bs4 import BeautifulSoup

with open('web02.html', mode = 'r', encoding = 'UTF-8') as f:
    soup = BeautifulSoup(f, 'html5lib')
    # print(soup)

    # HTML 문서 안에 있는 모든 div 태그를 찾음
    for div in soup('div'):  # soup('div')와 soup.find_all('div')는 동일
        print(div.text)

    # HTML 문서 안의 'class1' 속성을 갖는 모든 요소들을 찾음
    # soup(attrs = {attr이름: attr값})
    # soup.find_all(attrs = {attr이름: attr값})

    # for class1 in soup.find_all(attrs = {'class': 'class1'}):
    for class1 in soup(attrs = {'class1'}):
        print(class1.text)

    print()
    # HTML 문서 안의 'class2' 클래스 속성을 갖는 모든 요소들을 찾음
    # for cls_2 in soup.find_all(class_ = 'class2'):
    for cls_2 in soup(class_ = 'class2'):
        print(cls_2)

    print()
    # HTML 문서 안의 'id1' 아이디 속성을 갖는 요소를 찾음
    print(soup.find(id = 'id1'))
    print(soup.find(id = 'id1').text)
    print(soup(id = 'id1')[0].text)  # find_all

    # for id in soup(id = 'id1'):
    #     print(id)


