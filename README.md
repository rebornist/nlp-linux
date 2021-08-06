# 자연어 처리

## konlpy 설치

- pip install konlpy
- (konlpy 설치 실패 시)conda install -c conda-forge jpype1

## Mecab 설치

- bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

## gcc 설치

- brew install gcc

## subword-nmt 가져오기

- git clone https://github.com/kh-kim/subword-nmt.git

## 띄어쓰기 전처리 - pykospacing
- pip install git+https://github.com/haven-jeon/PyKoSpacing.git

```py
from pykospacing import spacing 
print(spacing("김형호영화시장분석가는'1987'의네이버영화정보네티즌10점평에서언급된단어들을지난해12월27일부터올해1월10일까지통계프로그램R과KoNLP패키지로텍스트마이닝하여분석했다."))
출처: https://ebbnflow.tistory.com/246 [Dev Log : 삶은 확률의 구름]
```

## 문장 분리 전차리 - kss
- pip install kss

```py
import kss 
s = "회사 동료 분들과 다녀왔는데 분위기도 좋고 음식도 맛있었어요 다만, 강남 토끼정이 강남 쉑쉑버거 골목길로 쭉 올라가야 하는데 다들 쉑쉑버거의 유혹에 넘어갈 뻔 했답니다 강남역 맛집 토끼정의 외부 모습." 
for sent in kss.split_sentences(s): 
    print(sent)
```

## 맞춤법 검사기 - py-hanspell
- pip install py-hanspell
```py
from hanspell import spell_checker 
result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.')
result.as_dict() # dict로 출력 
{
    'checked': '안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.', 
    'errors': 4, 'original': '안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.',
    'result': True, 'time': 0.07065701484680176,
    'words': {
        '안녕하세요.': 2, '저는': 0, '한국인입니다.': 2, '이': 2, '문장은': 2, '한글로': 0, '작성됐습니다.': 1
    }
} 
>>> result 
Checked(
    result=True,
    original='안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.', 
    checked='안녕하세요. 저는 한국인입니다. 이 문장은 한글로 작성됐습니다.',
    errors=4, 
    words=OrderedDict(
        [
            ('안녕하세요.', 2),
            ('저는', 0),
            ('한국인입니다.', 2),
            ('이', 2),
            ('문장은', 2),
            ('한글로', 0),
            ('작성됐습니다.', 1)
        ]
    ),
    time=0.10472893714904785)
```

### 파리미터
    1. result 맞춤법 검사 성공여부를 나타냅니다. 
    2. original 검사 전의 문장입니다. c
    3. hecked 맞춤법 검사 후의 문장입니다. 
    4. errors 맞춤법 오류 수를 나타냅니다.
    5. words Checked.words time 총 요청 시간을 나타냅니다.


## 반복어 nomalize - soynlp
- pip install soynlp
```py
from soynlp.normalizer import * 
print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2))
```