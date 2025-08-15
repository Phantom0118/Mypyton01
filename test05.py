# คำสั่งรับข้อความ string ทางแป้นพิมพ์ ใช้ฟังก์ชั้นinput{}
# ****** ตัวแปร variable คือ ข้อที่ Dev ตั้งขึ้นมาเอง(ต้องเป็นไปตามกฎการตั้งชื่อ)เอาไว้เก็บข้อมูลที่เกิดขึ้นในโปรแกรม

fullname = input('ป้อนชื่อ: ')
year_born = input('ป้อนปีเกิด พ.ศ.: ')
print('-----------------------')
print(f'สวัสดีคุณ {fullname}')
print(f'คุณเกิดในปี {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)}')
# ใช้ , 
print('-----------------------')
print('สวัสดีคุณ',fullname)
print('คุณเกิดในปี',year_born,' ตอนนี้คุณอายุ',2568 - int(year_born))
#ใช้  + 
print('-----------------------')
print('สวัสดีคุณ'+fullname)
print('คุณเกิดในปี'+year_born+' ตอนนี้คุณอายุ'+str(2568 - int(year_born)))
# ใช้ format
print('-----------------------')
print('สวัสดีคุณ {}'.format(fullname))
print('คุณเกิดในปี {}'.format(year_born) +' ตอนนี้คุณอายุ {}'.format(2568 - int(year_born)))