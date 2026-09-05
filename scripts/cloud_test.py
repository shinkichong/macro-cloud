  import requests
  from selenium import webdriver
  from selenium.webdriver.chrome.options import Options
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager

  print("=== Selenium (Google Chrome, headless) ===")
  opts = Options()
  opts.add_argument("--headless=new")
  opts.add_argument("--no-sandbox")
  opts.add_argument("--disable-dev-shm-usage")
  opts.binary_location = "/usr/bin/google-chrome"
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service, options=opts)
  try:
      targets = [
          ("10년/5년 국채선물지수 페이지", "https://index.krx.co.kr/contents/MKD/03/0305/03050100/MKD03050100.jsp"),
          ("VKOSPI 페이지", "https://index.krx.co.kr/contents/MKD/03/0305/03050200/MKD03050200.jsp"),
          ("KOSPI 차트 (네이버)", "https://m.stock.naver.com/fchart/domestic/index/KOSPI"),
      ]
      for name, url in targets:
          try:
              driver.get(url)
              print(f"[OK] {name}: title={driver.title!r} html_len={len(driver.page_source)}")
          except Exception as e:
              print(f"[FAIL] {name}: {e}")
  finally:
      driver.quit()

  print("\n=== requests 접근성 확인 (로그인/인증 시도 없음) ===")
  checks = [
      ("kakao API 서버", "https://kapi.kakao.com"),
      ("KRX 투자자별거래실적 화면(로그인 필요 예상)", "https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201"),
  ]
  for name, url in checks:
      try:
          r = requests.get(url, timeout=10)
          print(f"[OK] {name}: status={r.status_code} len={len(r.text)}")
      except Exception as e:
          print(f"[FAIL] {name}: {e}")
