def CAGR_FORMULA(start_price,future_estimated_price,time):
    cagr=(future_estimated_price/start_price)**(1/time)-1
    return round(cagr*100,2)
print('META 10 year CAGR analysis:')
print('='*50)
conservative_result=CAGR_FORMULA(1.63,3.63,10)#for META
print(f'Conservative CAGR for meta for 10 years:{conservative_result}%')
realistic_result=CAGR_FORMULA(1.63,5.07,10)
print(f'Realistic CAGR for meta for 10 years:{realistic_result}%')
optimistic_result=CAGR_FORMULA(1.63,6.61,10)
print(f'Optimistic CAGR for meta for 10 years:{optimistic_result}%')