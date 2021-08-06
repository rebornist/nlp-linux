# 텍스트 전처리 기능 자동화

- with anaconda, mecab, konlpy, etc ...

## Konlpy 설치

- [JDK 설치](https://www.oracle.com/kr/java/technologies/javase/javase-jdk8-downloads.html)
- Anaconda Powershell Prompt 관리자 권한으로 실행
- conda create -n textMining python=3.6 anaconda
- conda activate textMining
- [konlpy 설치](https://konlpy-ko.readthedocs.io/ko)
- pip install --upgrade pip
- pip install JPype1-0.5.7-cp27-none-win_amd64.whl
- pip install konlpy
- [Mecab 설치](https://cleancode-ws.tistory.com/97)

## subword-nmt 사용법

- cut -f2 ./output/output_1626648295.refined.tokenized.tsv > ./output/output.refined.tokenized.tsv.text
- cat ./output/output.refined.tokenized.tsv.text | mecab -O wakati | python post_tokenize.py ./output/output.refined.tokenized.tsv.text > ./output/output.refined.tokenized.tsv.text.tok
- python ./subword/learn_bpe.py --input ./output/output.refined.tokenized.tsv.text.tok --output ./model --symbols 30000
- python ./subword/apply_bpe.py --codes ./model < ./output/output.refined.tokenized.tsv.text.tok > ./output/output.refined.tokenized.tsv.text.tok.bpe
- cut -f1 ./output/output_1626648295.refined.tsv > ./output/output_1626648295.refined.tsv.label
- paste ./output/output_1626648295.refined.tsv.label ./output/output.refined.tokenized.tsv.text.tok.bpe > ./output/output.refined.tokenized.tsv.text.tok.bpe.tsv

## detokenization 사용법

- python ./subword/detokenizer.py < ./output/output.refined.tok.tsv.text.bpe.tsv > ./output/output.refined.tok.tsv.text.bpe.detok.tsv

## pytorch 사용법

- 해당 파일 확인
- wc -l ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok\*
- gshuf < ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.tsv > ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.shuf.tsv
- head -n 157260 ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.shuf.tsv > ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.shuf.train.tsv
- head -n 10000 ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.shuf.tsv > ./preprocessing/output/output.refined.tok.tsv.text.bpe.detok.shuf.test.tsv
