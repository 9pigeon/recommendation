from flask import Flask, request, jsonify

app = Flask(__name__)

# 가상의 상품 데이터셋 (예시)
product_data = {
        "product1": {
            "fin_prdt_cd": "WR0001B",
            "spcl_cnd": "해당사항 없음"
        },
        "product2": {
            "fin_prdt_cd": "00320342",
            "spcl_cnd": "1.SC제일은행 최초 거래 신규고객에 대하여 우대 이율을 제공함 (보너스이율0.2%)                     2.SC제일마이백통장에서 출금하여 이 예금을 신규하는경우에 보너스이율을 제공함\n(가입기간:1년제/ 보너스이율:0.1% / 만기해약하는 경우에 한해 보너스이율을 적용함)"
        },
        "product3": {
            "fin_prdt_cd": "10511008000996000",
            "spcl_cnd": "최고우대금리 : 연0.65%p              \n - 목돈굴리기예금 최초 가입시 : 연0.20%p\n - 상품 가입 전 최근 1개월 이내 신용(체크)카드 신규 발급 : 연0.20%p\n - 상품 가입 전 최근 1개월 이내 인터넷.폰.스마트뱅킹 가입 : 연0.20%p\n * 해당 상품을 인터넷/스마트뱅킹을 통해 가입 : 연0.05%p"
        },
        "product4": {
            "fin_prdt_cd": "10511008001004000",
            "spcl_cnd": "최고우대금리 : 연0.45%p\n- 지난달 대구은행 통장으로 연금 입금 실적 보유 : 연0.10%p\n- 상품 가입 전 대구은행 신용(체크)카드 보유 : 연0.10%p\n- 지난 3개월 예금 평잔 30만원 이상 : 연0.10%p\n- DGB행복파트너적금 동시 가입 및 만기 보유 : 연0.10%p\n*해당상품을 인터넷/스마트뱅킹을 통해 가입 : 연0.05%p"
        },
        "product5": {
            "fin_prdt_cd": "10511008001166004",
            "spcl_cnd": "최고우대금리 : 연0.45%p\n-전월 총 수신 평잔실적 또는 상품 가입 전 첫만남플러스 통장 보유시 \n-대구은행 주택청약상품보유 \n-신규일 \"DGB함께적금\" 동시 가입 및 만기 보유 \n-대구은행 오픈뱅킹서비스에 다른 은행 계좌 등록시 각 연0.10%p                       \n*해당상품을 인터넷/스마트뱅킹을 통해 가입 시 : 연0.05%p"
        },
        "product6": {
            "fin_prdt_cd": "10511008001278000",
            "spcl_cnd": "최고우대금리 : 연0.25%p\n- 가입일(재예치일)로부터 3개월이내 아래 1가지 이상 요건 충족시\n① DGB대구은행 주택청약종합저축 보유\n② DGB대구은행 신용(체크)카드 결제실적 보유(결제금액 출금기준)\n* 해당 상품을 인터넷/스마트뱅크를 통해 가입 : 연0.05%p"
        },
        "product7": {
            "fin_prdt_cd": "01030500510002",
            "spcl_cnd": "*우대이율\n가. 3~5개월 특판우대이율 : 0.95%\n나. 6~11개월 특판 우대이율: 0.85%\n다. 12개월 특판 우대이율 : 0.65%"
        },
        "product8": {
            "fin_prdt_cd": "01030500560002",
            "spcl_cnd": "* 우대이율 (최대 0.75%p)\n가. 모바일뱅킹 금융정보 및 혜택알림 동의 우대이율 : 0.10%p\n나. 이벤트 우대이율 : 최대 0.65%p \n1) 더(The) 특판 정기예금 신규고객 우대이율 : 0.20%p\n2) 특판 우대이율 : 0.45%p"
        },
        "product9": {
            "fin_prdt_cd": "TD11300027000",
            "spcl_cnd": "▶ 최고우대금리 0.2% \n ① 요구불평잔 : 0.2% -300만원이상 0.1%, 500만원이상 0.2%\n ② 신용(체크)카드결제실적 : 0.1% -전월결제금 300만원이상 0.05%, 500만원이상 0.1%"
        },
        "product10": {
            "fin_prdt_cd": "TD11300031000",
            "spcl_cnd": "▶ 1천만원 이상 가입시"
        }
}



# 유사한 상품을 찾는 함수 (예시)
def find_similar_products(target_fin_prdt_cd):
    # 여기서는 가상의 유사 상품을 찾는 로직을 사용합니다.
    # 실제로는 여러 방법을 사용할 수 있습니다.
    similar_products = []
    for product_key, product_info in product_data.items():
        if product_info["fin_prdt_cd"] != target_fin_prdt_cd:
            similar_products.append(product_info["fin_prdt_cd"])
        if len(similar_products) >= 10:
            break
    return similar_products

# http://127.0.0.1:5000/recommendation?target_fin_prdt_cd=001
@app.route('/recommendation', methods=['GET'])
def get_similar_products():
    target_fin_prdt_cd = request.args.get('target_fin_prdt_cd')
    if target_fin_prdt_cd is None:
        return jsonify({"error": "Missing target_fin_prdt_cd parameter"}), 400

    similar_products = find_similar_products(target_fin_prdt_cd)

    return jsonify({"similar_products": similar_products})


if __name__ == '__main__':
    app.run(debug=True)
