# 배경 제거 API 서버

이미지에서 배경을 제거하는 간단한 API 서버입니다.

## 기능

- 이미지 업로드 시 배경 자동 제거
- 토큰 기반 인증
- RESTful API 설계

## 설치 및 실행

### 필요한 패키지 설치
```bash
pip install flask rembg pillow
```

### 서버 실행
```bash
python app.py
```

서버는 `http://localhost:8080`에서 실행됩니다.

## API 엔드포인트

### 배경 제거 API

**POST** `/api/remove-background`

#### 요청 형식
- **Content-Type**: `multipart/form-data`
- **파일**: `file` 필드에 이미지 파일 첨부
- **토큰**: 다음 중 하나의 방법으로 토큰 전송
  - Header: `Authorization: Bearer dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd`
  - Query Parameter: `?token=dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd`
  - Form Data: `token=dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd`

#### 응답
- **성공 (200)**: 배경이 제거된 PNG 이미지 파일
- **실패**: JSON 에러 메시지

## 사용 예시

### curl을 사용한 예시
```bash
# Header에 토큰 포함
curl -X POST \
  -H "Authorization: Bearer dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd" \
  -F "file=@image.jpg" \
  http://localhost:8080/api/remove-background \
  --output result.png

# Query parameter에 토큰 포함
curl -X POST \
  -F "file=@image.jpg" \
  "http://localhost:8080/api/remove-background?token=dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd" \
  --output result.png
```

### Python을 사용한 예시
```python
import requests

url = "http://localhost:8080/api/remove-background"
headers = {
    "Authorization": "Bearer dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd"
}

with open("input_image.jpg", "rb") as f:
    files = {"file": f}
    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        with open("output_image.png", "wb") as output:
            output.write(response.content)
        print("배경 제거 완료!")
    else:
        print("오류:", response.json())
```

## 에러 코드

- `INVALID_TOKEN`: 유효하지 않은 토큰
- `NO_FILE`: 파일이 업로드되지 않음
- `VALIDATION_ERROR`: 파일 유효성 검사 실패
- `PROCESSING_ERROR`: 이미지 처리 중 오류
- `NOT_FOUND`: 엔드포인트를 찾을 수 없음
- `METHOD_NOT_ALLOWED`: 허용되지 않은 HTTP 메서드

## 보안

토큰 `dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd`는 모든 API 요청에 필요합니다. 프로덕션 환경에서는 환경 변수로 관리하는 것을 권장합니다.