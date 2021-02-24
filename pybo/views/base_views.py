from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question

##########################################################
def index(request):
    '''
    pybo 목록 출력
    '''

    # order_by() : 조회한 데이터를 특정 속성으로 정렬  // -create_date : - 기호가 앞에 있으므로 역순 조회회

    # 입력 파라미터
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw','') #검색어
    so = request.GET.get('so','recent') #정렬기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # recent
        question_list = Question.objects.order_by('-create_date')


    # 조회

    if kw:
        question_list=question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색  _ 제목에 kw 문자열이 포함되었는지를 의미
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)   # 답변 글쓴이검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    #context = {'question_list': page_obj}
    context = {'question_list': page_obj, 'page':page, 'kw':kw, 'so':so} # page와 kw, so가 추가되었다.
    return render(request, 'pybo/question_list.html', context)

    #pybo/question_list.html : question_list를 HTML로 변환
    #위와 같은 형식을 '템플릿' 이라 부른다.

##########################################################

def detail(request, question_id):
    '''
    pybo 내용 출력
    '''
    question = get_object_or_404(Question, pk=question_id)
    # 페이지가 존재하지 않으면 404 페이지 출력
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
#'''
#응답 오류 코드
#200 : 성공
#500 : 서버 오류 (Internal Server Error)
#404 : 페이지 존재하지 않음 (Not Found)
#'''