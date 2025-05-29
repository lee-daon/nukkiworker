import requests
import os
from datetime import datetime

# API 서버 설정 - Cloud Run URL (포트 번호 제거)
API_URL = "https://rembg-api-626680981853.asia-northeast3.run.app/api/remove-background"
TOKEN = "dsablcvwahdbhsabc1834bkjewpfubaiu42tjhrbufbd"

def test_with_header_token(image_path):
    """
    Authorization 헤더에 토큰을 포함하여 테스트
    """
    print("=== Authorization 헤더 토큰 테스트 ===")
    
    if not os.path.exists(image_path):
        print(f"❌ 테스트 이미지 파일을 찾을 수 없습니다: {image_path}")
        return False
    
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            print(f"📤 요청 전송 중... ({image_path})")
            response = requests.post(API_URL, headers=headers, files=files, timeout=60)
            
        if response.status_code == 200:
            # 성공적으로 처리된 경우
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"output_header_{timestamp}.png"
            
            with open(output_filename, "wb") as output:
                output.write(response.content)
            
            print(f"✅ 성공! 결과 이미지가 저장되었습니다: {output_filename}")
            print(f"📝 응답 헤더: {dict(response.headers)}")
            return True
        else:
            print(f"❌ 실패 (상태코드: {response.status_code})")
            try:
                error_info = response.json()
                print(f"📝 에러 정보: {error_info}")
            except:
                print(f"📝 응답 내용: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 요청 중 오류 발생: {str(e)}")
        return False

def test_with_query_token(image_path):
    """
    쿼리 파라미터에 토큰을 포함하여 테스트
    """
    print("\n=== 쿼리 파라미터 토큰 테스트 ===")
    
    if not os.path.exists(image_path):
        print(f"❌ 테스트 이미지 파일을 찾을 수 없습니다: {image_path}")
        return False
    
    url_with_token = f"{API_URL}?token={TOKEN}"
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            print(f"📤 요청 전송 중... ({image_path})")
            response = requests.post(url_with_token, files=files, timeout=60)
            
        if response.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"output_query_{timestamp}.png"
            
            with open(output_filename, "wb") as output:
                output.write(response.content)
            
            print(f"✅ 성공! 결과 이미지가 저장되었습니다: {output_filename}")
            return True
        else:
            print(f"❌ 실패 (상태코드: {response.status_code})")
            try:
                error_info = response.json()
                print(f"📝 에러 정보: {error_info}")
            except:
                print(f"📝 응답 내용: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 요청 중 오류 발생: {str(e)}")
        return False

def test_with_form_token(image_path):
    """
    Form data에 토큰을 포함하여 테스트
    """
    print("\n=== Form Data 토큰 테스트 ===")
    
    if not os.path.exists(image_path):
        print(f"❌ 테스트 이미지 파일을 찾을 수 없습니다: {image_path}")
        return False
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            data = {"token": TOKEN}
            print(f"📤 요청 전송 중... ({image_path})")
            response = requests.post(API_URL, files=files, data=data, timeout=60)
            
        if response.status_code == 200:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"output_form_{timestamp}.png"
            
            with open(output_filename, "wb") as output:
                output.write(response.content)
            
            print(f"✅ 성공! 결과 이미지가 저장되었습니다: {output_filename}")
            return True
        else:
            print(f"❌ 실패 (상태코드: {response.status_code})")
            try:
                error_info = response.json()
                print(f"📝 에러 정보: {error_info}")
            except:
                print(f"📝 응답 내용: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 요청 중 오류 발생: {str(e)}")
        return False

def test_invalid_token(image_path):
    """
    잘못된 토큰으로 테스트 (에러 응답 확인)
    """
    print("\n=== 잘못된 토큰 테스트 ===")
    
    if not os.path.exists(image_path):
        print(f"❌ 테스트 이미지 파일을 찾을 수 없습니다: {image_path}")
        return False
    
    headers = {
        "Authorization": "Bearer invalid_token_123"
    }
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            print(f"📤 잘못된 토큰으로 요청 전송 중...")
            response = requests.post(API_URL, headers=headers, files=files, timeout=60)
            
        if response.status_code == 401:
            print("✅ 예상대로 401 Unauthorized 응답을 받았습니다.")
            try:
                error_info = response.json()
                print(f"📝 에러 정보: {error_info}")
            except:
                print(f"📝 응답 내용: {response.text}")
            return True
        else:
            print(f"❌ 예상과 다른 응답 (상태코드: {response.status_code})")
            return False
            
    except Exception as e:
        print(f"❌ 요청 중 오류 발생: {str(e)}")
        return False

def test_server_connection():
    """
    서버 연결 상태 확인
    """
    print("=== 서버 연결 테스트 ===")
    try:
        # Cloud Run 서버의 루트 경로 확인
        base_url = API_URL.replace('/api/remove-background', '')
        response = requests.get(base_url, timeout=10)
        print("✅ 서버에 연결되었습니다.")
        return True
    except requests.exceptions.ConnectionError:
        print("❌ 서버에 연결할 수 없습니다. Cloud Run 서비스가 실행 중인지 확인해주세요.")
        return False
    except Exception as e:
        print(f"❌ 연결 테스트 중 오류 발생: {str(e)}")
        return False

def main():
    print("🚀 배경 제거 API 서버 테스트를 시작합니다.")
    print(f"📍 API URL: {API_URL}")
    
    # 서버 연결 확인
    if not test_server_connection():
        return
    
    # 테스트할 이미지 파일 경로 입력받기
    image_path = input("\n📁 테스트할 이미지 파일 경로를 입력해주세요 (예: test_image.jpg): ").strip()
    
    if not image_path:
        print("❌ 이미지 파일 경로가 입력되지 않았습니다.")
        return
    
    # 각 방법별로 테스트 실행
    success_count = 0
    
    if test_with_header_token(image_path):
        success_count += 1
    
    if test_with_query_token(image_path):
        success_count += 1
        
    if test_with_form_token(image_path):
        success_count += 1
    
    if test_invalid_token(image_path):
        success_count += 1
    
    print(f"\n📊 테스트 결과: {success_count}/4 개 테스트 통과")
    
    if success_count == 4:
        print("🎉 모든 테스트가 성공적으로 완료되었습니다!")
    else:
        print("⚠️  일부 테스트가 실패했습니다. 서버 상태를 확인해주세요.")

if __name__ == "__main__":
    main()
