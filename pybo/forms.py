from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    '''
    장고 폼
    forms.Form : 폼
    forms.ModelForm : 모델 폼 _ 모델과 연결된 폼, 아래의 meta 클래스를 반드시 가져야 한다.
    '''
    class Meta: # 모델 폼이 사용할 모델과 모델의 필드들을 적어야한다.
        model = Question
        fields = ['subject', 'content']

        #widgets = {
        #    'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        #}


        # 수작업으로 폼 작성
        labels = {
            'subject': '제목',
            'content': '내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }