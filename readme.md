# ez-image-optimizer

디자이너와 개발자를 위한 이미지크기를 쉽게 자동으로 줄여주는 간단한 프로그램입니다.

# Windows 실행파일 다운로드

dist 경로 안에 있는 exe 파일을 사용하시거나 pyinstaller로 exe를 만들어보세요.

# 필요 모듈 설치방법
```python
pip install pillow
```

# 사용방법

### CLI mode

```bash
usage: ez-image-optimizer.py [-h] [-f F]

optional arguments:
  -h, --help  show this help message and exit
  -f F        Specific Image file path to convert.
              Basically, If do not use it,
              [./img/*] images will be optimized in [./img-optimized]
              or change conf.py
```


### exe 파일

1. dist 경로에 ez-image-optimizer.zip 파일의 압축을 풉니다.

2. 그후 변경하실 이미지들을 img 폴더에 넣고 exe 파일을 실행합니다.

3. img-optimized 경로 안에 용량이 줄어든 이미지 파일들이 생성됩니다.


### 설정

conf.py 안의 설정값들을 적절하게 조절합니다.

아래는 기본소스입니다.

```python
# default configure

image_config = {
    "quality":85,
    "max_dimension":1000,
    "optimize_into_jpg":True,
    "origin_img_dir_path":"img/",
    "optimized_img_dir_path":"img-optimized/"
}
```

* 'quality' 는 0~100까지 조절할 수 있으며 높을수록 고품질 고용량입니다. jpg경우에 85 정도가 적당합니다.

* 'max_dimension' 은 이미지의 최대크기입니다. 변경 후 이미지의 크기는 원본크기를 넘을 수 없으며, 가로 또는 세로의 긴 축을 기준으로 max_dimension 값을 넘지 못합니다.

* 'optimize_into_jpg' 는 pillow 모듈이 인식 가능한 이미지 형식들을 모두 jpg 형식으로 압축합니다. 예를들어 True 설정 시 png, bmp 확장자의 이미지들도 jpg 형식으로 변경되며 확장자도 변경됩니다.

* 'origin_img_dir_path' 는 원본 경로입니다. 실행파일 기준으로 상대경로로 설정하여 주세요.

* 'optimized_img_dir_path' 는 변환 후 이미지가 저장될 경로입니다. 실행파일 기준으로 상대경로로 설정하여 주세요.