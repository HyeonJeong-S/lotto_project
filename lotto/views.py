from django.shortcuts import render, redirect
from .models import LottoTicket, LottoDraw
import random

def index(request):
    return render(request, "lotto/index.html")

def buy_lotto(request):
    if request.method == "POST":
        user = request.POST.get("user")
        mode = request.POST.get("mode")
        numbers = request.POST.get("numbers", "")

        last_draw = LottoDraw.objects.order_by('-round').first()
        round_num = last_draw.round + 1 if last_draw else 1
 
        if mode == "auto":
            numbers_list = sorted(random.sample(range(1,46), 6))
            numbers = ", ".join(map(str, numbers_list))
        else:
            temp = numbers.replace(",", " ").split()
            
            try:
                numbers_list = [int(n) for n in temp]
            except:
                return render(request, "lotto/buy.html", {
                    "error": "숫자만 입력할 수 있습니다!"
                })
 
            if len(numbers_list) != 6:
                return render(request, "lotto/buy.html", {
                    "error": "숫자 6개를 입력해야 합니다!"
                })
 
            if any(n < 1 or n > 45 for n in numbers_list):
                return render(request, "lotto/buy.html", {
                    "error": "모든 번호는 1~45 사이여야 합니다!"
                })
 
            if len(set(numbers_list)) !=6:
                return render(request, "lotto/buy.html", {
                    "error": "중복된 번호가 있습니다!"
                })
 
            numbers_list = sorted(numbers_list)
            numbers = ", ".join(map(str, numbers_list))
     
        LottoTicket.objects.create(user=user, numbers=numbers, round=round_num)
        return render(request, "lotto/buy_result.html", {
            "numbers": numbers,
            "user": user,
            "round": round_num
        })
    return render(request, "lotto/buy.html")

def draw_numbers(request):
    if request.method == "POST":
        last_draw = LottoDraw.objects.order_by('-round').first()
        round_num = last_draw.round + 1 if last_draw else 1
        winning_numbers_list = random.sample(range(1, 46), 6)
        winning_numbers = ", ".join(str(n) for n in sorted(winning_numbers_list))
        draw = LottoDraw.objects.create(round=round_num, winning_numbers=winning_numbers)
        return render(request, "lotto/draw_result.html", {"winning_numbers": winning_numbers, "round": round_num})
   
    return render(request, "lotto/draw.html")

def check_result_page(request):
    if request.method == "POST":
        try:
            round_num = request.POST.get("round")
        except (TypeError, ValueError):        
            round_num = 1

        return redirect("check_result", round=round_num)
    return render(request, "lotto/check_result_page.html")

def check_result(request, round):
    try:
        draw = LottoDraw.objects.get(round=round)
    except LottoDraw.DoesNotExist:
        return render(request, "lotto/check_result.html", {
            "error": f"{round}회차의 추첨 기록이 없습니다."
        })
   
    tickets = LottoTicket.objects.filter(round=draw.round)
    results = []
    winning_numbers = set(map(int, draw.winning_numbers.split(", ")))

    for t in tickets:
        ticket_numbers = set(map(int, t.numbers.split(", ")))
        matched = len(ticket_numbers & winning_numbers)
        results.append({"ticket": t.numbers, "matched": matched})
    
    return render(request, "lotto/check_result.html", {
        "round": round,
        "draw": draw,
        "results": results
    })
