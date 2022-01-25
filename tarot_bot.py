import random
import telebot

token = '5097614944:AAH8Ha0UVZ2DuuqYSLps840EtTNh4_eXWVY'

bot = telebot.TeleBot(token)

major_arcana = ['CAACAgEAAxkBAAEDtU5h5w8KbCjoYn_pbDn0qBa87uYJKQACGwADH2dzDMXzYfhEirjjIwQ', #0 the fool
'CAACAgEAAxkBAAEDtVBh5w-B4zID59ZcVKFchx_dixQN_gACHQADH2dzDI488Wi5wL5tIwQ', #1 the magician
'CAACAgEAAxkBAAEDtVRh5xAD1EGyJuJpgXfrrLEZ-WypsgACIAADH2dzDETLDonNx9oHIwQ', #2 the high priestess
'CAACAgEAAxkBAAEDtVZh5xBgymjtrUqdLwo408ljGtuDRgACIwADH2dzDLZRsSYS2DF3IwQ', #3 the empress
'CAACAgEAAxkBAAEDtWFh5xEvrnOrOqL8v70fM8H5UHwRtwACJQADH2dzDMaOvG-_q5leIwQ', #4 the emperor
'CAACAgEAAxkBAAEDtWNh5xI9PfgGnZiFzLzVPexCFKPwigACJwADH2dzDFY_7woVWGKAIwQ', #5 the hierophant
'CAACAgEAAxkBAAEDtXNh5xLvhZRNCmCelm4T94wc6ug5XAACKQADH2dzDORmhCTTR3ExIwQ', #6 the lovers
'CAACAgEAAxkBAAEDtYdh5xSYYsSOdRMUiOrHrvAU7UhitQACKwADH2dzDFNNbIZJ65cXIwQ', #7 the chariot
'CAACAgEAAxkBAAEDtZNh5xkRLZDu15e0sccNaL6SU1ZsFAACLQADH2dzDIP04lzcth9HIwQ', #8 strength
'CAACAgEAAxkBAAEDtZVh5xmBj1ACOvAc1ddVHY5SaO32QwACLwADH2dzDOsPTnYjza_-IwQ', #9 the hermit
'CAACAgEAAxkBAAEDtZdh5xnmwLvSy3_wmDI4eMnFgd8JBQACMQADH2dzDCEnuXKtAl2fIwQ', #10 wheel of fortune
'CAACAgEAAxkBAAEDtZlh5xo0m67c7KQMS5UzY3NBrkKfBQACMwADH2dzDOFdbG-zARTPIwQ', #11 justice
'CAACAgEAAxkBAAEDtZth5xqI5sLMpxqpQuxowMfpb3GMngACNQADH2dzDHTlbsvwVszAIwQ', #12 the hanged man
'CAACAgEAAxkBAAEDtZ1h5xreDvMJIgRXM9c6xD8ao8dKywACNwADH2dzDDnTb5m3UepeIwQ', #13 death
'CAACAgEAAxkBAAEDtZ9h5xtALIsEVp20DUxu9u1KPvzGwAACOQADH2dzDJd-nEVwq4VYIwQ', #14 temperance
'CAACAgEAAxkBAAEDtaFh5xurw1yZOv0HiSq7bpq1V5_9bwACOwADH2dzDN3IE8OPRqq3IwQ', #15 the devil
'CAACAgEAAxkBAAEDtaNh5xwAAbh93eLTknHBptxWiIEZuHkAAj0AAx9ncwyFAAFXv9h3aywjBA', #16 the tower
'CAACAgEAAxkBAAEDtaVh5xxfbDrTOND4Wx6rCxa9edt4HAACPwADH2dzDCo8tyby63LLIwQ', #17 the star
'CAACAgEAAxkBAAEDtadh5xyoEsn2wHbEoM0P3iUkboP4KQACQQADH2dzDInQC1Of31-WIwQ', #18 the moon
'CAACAgEAAxkBAAEDtalh5x0N16QqHA4y2GkzQnEg_a71ggACQwADH2dzDLbrqBWw3JZbIwQ', #19 the sun
'CAACAgEAAxkBAAEDtath5x2OS2smBuuhI5YAAYDZ1iFcllQAAkUAAx9ncwzXiIm-uBpvYCME', #20 judgement
'CAACAgEAAxkBAAEDta1h5x3ReswzQ-J10yPsmBxDdTyfkgACRwADH2dzDFkz0WITRl_ZIwQ'] #21 the world

minor_arcana = ['CAACAgEAAxkBAAEDta9h5x5EmIs4n47FmiFd_iPP4qgfkAACSgADH2dzDGuQIzLuwbGeIwQ', #Ace of Wands
'CAACAgEAAxkBAAEDt8lh6I2gyPCWLhk1vgqY0rZSfo0EwgACTAADH2dzDFvcgYfVLVVgIwQ', #Two of Wands
'CAACAgEAAxkBAAEDt8th6I4RyhfCLaoBkrML2_C-u5AORwACTgADH2dzDDwhvRKEcHu9IwQ', #Three of Wands
'CAACAgEAAxkBAAEDt81h6I5pYEsuSZAXYgZ5iKRrH4ExAwACUAADH2dzDMhM1-R09WgrIwQ', #Four of Wands
'CAACAgEAAxkBAAEDt9Zh6I7I1QgJHQh_4gUwtdEdFsCBfQACUgADH2dzDG_E1u7jKKtlIwQ', #Five of Wands
'CAACAgEAAxkBAAEDt9hh6I8uxVnZTEVCGqW9JzZ9hNFSYAACVAADH2dzDGhnh_xEHoNhIwQ', #Six of Wands
'CAACAgEAAxkBAAEDt9ph6I9ew2ScGGAkYjSuA59i8LiqFAACVgADH2dzDE4t2_xtzsWZIwQ', #Seven of Wands
'CAACAgEAAxkBAAEDt9xh6I_prjSBdP5_obH5HHEOtJyvTgACWAADH2dzDDVsaNUri5crIwQ', #Eight of Wands
'CAACAgEAAxkBAAEDt95h6JA74gl42Cs9RIA6I6ISQuk13wACWgADH2dzDOOL7IE707mtIwQ', #Nine of Wands
'CAACAgEAAxkBAAEDt-Bh6JCNBzVhVruwVuW0IBNnuYev2wACXAADH2dzDA5NlGVGWXDQIwQ', #Ten of Wands
'CAACAgEAAxkBAAEDt-Jh6JFbS2nCytnWx4a4PnTHKJGbtgACXgADH2dzDHYi-FrecG5YIwQ', #Page of Wands
'CAACAgEAAxkBAAEDt-Rh6JG3K_DMthm6L82mYjaJDGrEbgACYAADH2dzDNmr51NCf80fIwQ', #Knight of Wands
'CAACAgEAAxkBAAEDt-Zh6JIAATQqiDfdFskqMTFBG4JcF5MAAmIAAx9ncwznJUl8M6KGrCME', #Queen of Wands
'CAACAgEAAxkBAAEDt-hh6JJbkUQ68gqRMTEBG01tl0BpUQACZAADH2dzDOmWawVom1GZIwQ', #King of Wands
'CAACAgEAAxkBAAEDuKBh6YZfSo4O7WJGsuvtB9lj3GQRHgACoAADH2dzDIhdeaHI24QMIwQ', #Ace of Pentacles
'CAACAgEAAxkBAAEDuKJh6YbS5XqUsqg3ZjURatOiuoDtaQACogADH2dzDLwOGX32aoYGIwQ', #Two of Pentacles
'CAACAgEAAxkBAAEDuKxh6YcWUrrK0WLlPl0dy2sS9Ekt5wACpAADH2dzDK_9gW6m_UIHIwQ', #Three of Pentacles
'CAACAgEAAxkBAAEDuLBh6Ydm_dkyhvpnt1MH6fSQYA5p3gACpgADH2dzDBl-zQXJXBsoIwQ', #Four of Pentacles
'CAACAgEAAxkBAAEDuLJh6Ye5pYLrLGvBGolsz8ydt2yfSAACqAADH2dzDBXrsVY4DWdTIwQ', #Five of Pentacles
'CAACAgEAAxkBAAEDuLRh6Ygtf81v0ceQuu6Q86rekRD3pQACqgADH2dzDKG5ypEngaa0IwQ', #Six of Pentacles
'CAACAgEAAxkBAAEDuLZh6YiEYk73Viut9oMVOV06vHA9sAACrAADH2dzDC-HngI-X34qIwQ', #Seven of Pentacles
'CAACAgEAAxkBAAEDuLhh6YjNeDwta_pf0pnNKYsHluxoNAACrgADH2dzDIT5uu2GOP9FIwQ', #Eight of Pentacles
'CAACAgEAAxkBAAEDuLph6YkzFXI3Dt39-ognmdKfa3cP4AACsAADH2dzDMiMQ6kCrOJxIwQ', #Nine of Pentacles
'CAACAgEAAxkBAAEDuLxh6Ylywwii2rwS4hGLmJvNR90cpQACsgADH2dzDNQCNbwCRRS9IwQ', #Ten of Pentacles
'CAACAgEAAxkBAAEDuMBh6Ym4DYeQRQY7joxjDjPh_ghXCwACtAADH2dzDOQ-UTtPV8EeIwQ', #Page of Pentacles
'CAACAgEAAxkBAAEDuMJh6YoHfxkYlAyjm-ZHd80QUnkJOAACtgADH2dzDDPmiAzdUtAvIwQ', #Knight of Pentacles
'CAACAgEAAxkBAAEDuMRh6YpaGksCLxtA0p3YUV-sYY742wACuAADH2dzDOazAvkOF2OWIwQ', #Queen of Pentacles
'CAACAgEAAxkBAAEDuMZh6YqzoG0yA-RZiRYS-QZkfJsvnwACugADH2dzDIsxa67pHGKAIwQ', #King of Pentacles
'CAACAgEAAxkBAAEDvDZh7PLKDMo1mh-RimAyyxWAn50PWAACagADH2dzDBthyEiYluJlIwQ', #Ace of Cups
'CAACAgEAAxkBAAEDvDhh7PP25JvDYN-IODEKYa_x4biJWwACbAADH2dzDKjXGr331BD4IwQ', #Two of Cups
'CAACAgEAAxkBAAEDvDph7PRcrLYUhoPcLk_8pm8m_BlygQACbgADH2dzDB-OLkXTtarVIwQ', #Three of Cups
'CCAACAgEAAxkBAAEDvDxh7PSpPRly4LlVjWnd8Flxlk_IVgACcAADH2dzDOxL9bX648ySIwQ', #Four of Cups
'CAACAgEAAxkBAAEDvD5h7PTtzUKaJA-otNP_s1hM96ySfAACcgADH2dzDLwXgBqI7HA5IwQ', #Five of Cups
'CAACAgEAAxkBAAEDvEBh7PU59EwYGayDvmIUkHeQ2ocCPgACvwADH2dzDJT3AS9ko4jtIwQ', #Six of Cups
'CAACAgEAAxkBAAEDvEZh7PWCPFJIwfzDKocMIbAaVys-9AACdQADH2dzDKkdLcMusdxaIwQ', #Seven of Cups
'CAACAgEAAxkBAAEDvEhh7PXJxZkTRGdTqU-XVQyuuDib0AACdwADH2dzDBu1p_GPKh75IwQ', #Eight of Cups
'CAACAgEAAxkBAAEDvEph7PYVcyw_wmHT_B_1WpgTJb3NbgACeQADH2dzDB1B1wxfwQPmIwQ', #Nine of Cups
'CAACAgEAAxkBAAEDvExh7PZUY-17q6P7Re69n6K_XQmhdQACewADH2dzDOqbbVvUHSXDIwQ', #Ten of Cups
'CAACAgEAAxkBAAEDvE5h7ParX4IcUzubM6PvErRdCR7gAgACfQADH2dzDBM7_FWWRXxBIwQ', #Page of Cups
'CAACAgEAAxkBAAEDvFBh7Pb57IjULgZD0eGh3eRu8-YDYwACfwADH2dzDHYrngyUmai1IwQ', #Knight of Cups
'CAACAgEAAxkBAAEDvFJh7PdAmkev30D_VDYh-HGeJLuLCAACgQADH2dzDFE94mDpjPEaIwQ', #Queen of Cups
'CAACAgEAAxkBAAEDvFRh7PejUIhRPdLLZEoPVvRAlV-4OAACgwADH2dzDCn4uKYfnb4uIwQ', #King of Cups
'CAACAgEAAxkBAAEDvr1h749U1cX4t_kIFoL2pqntRnPIkQAChQADH2dzDM83kd-d-DDYIwQ', #Ace of Swords
'CAACAgEAAxkBAAEDvr9h75A0wlweMD4hS8XbBsddefocAAOHAAMfZ3MMZ6oP_tZO8XojBA', #Two of Swords
'CAACAgEAAxkBAAEDvsFh75BrUB-C9o_ogXJI3w3e0xr_9QACiQADH2dzDKPwSEmOKPWfIwQ', #Three of Swords
'CAACAgEAAxkBAAEDvsNh75ClGe0DEOTdVFxunFHgjFe47gACiwADH2dzDB-nVJvr2WyIIwQ', #Four of Swords
'CAACAgEAAxkBAAEDvsVh75DoOBbSztbyNmzOy61tTlmtLwACjQADH2dzDISgJwABrlAGNCME', #Five of Swords
'CAACAgEAAxkBAAEDvsdh75EobRrg6CKp1cW62mUUFL9ceQACjwADH2dzDPE15owViHy-IwQ', #Six of Swords
'CAACAgEAAxkBAAEDvslh75FuRfOVXB5gTpqIFvN7wESGnQACkQADH2dzDItcROo08YF_IwQ', #Seven of Swords
'CAACAgEAAxkBAAEDvsth75LKFZXmnwTZ74LXHpQbwJ0azAACkwADH2dzDBCrW-yt7HNvIwQ', #Eight of Swords
'CAACAgEAAxkBAAEDvs1h75L5ByiZGq633ut4JtbqLlQoLgAClQADH2dzDB69Pa8EYNGsIwQ', #Nine of Swords
'CAACAgEAAxkBAAEDvs9h75M5XHxHoKJVCnNtfDqqdQ7zHgAClwADH2dzDEGYfDXNualZIwQ', #Ten of Swords
'CAACAgEAAxkBAAEDvtFh75N57UQF-47syb5YVJb9fIaRoAACmQADH2dzDIYThhSXsi7JIwQ', #Page of Swords
'CAACAgEAAxkBAAEDvtNh75PKno1i8xWy2D8IrGwaXsQvIwACwQADH2dzDB-8yNa63f3hIwQ', #Knight of Swords
'CAACAgEAAxkBAAEDvtVh75QKEQ4RJ-i7WgY6izo4zdkO2wACnAADH2dzDMeVM99NWWBtIwQ', #Queen of Swords
'CAACAgEAAxkBAAEDvtdh75RACEm-abidlp8s0VgoErsBZgACngADH2dzDEW7hiYLtWL7IwQ'] #King of Swords

all_cards = major_arcana + minor_arcana

@bot.message_handler(commands=['send_any'])
def all_sender(message):
    random_card_all = random.choice(all_cards)
    bot.send_sticker(message.chat.id, random_card_all)

@bot.message_handler(commands=['send_major'])
def major_sender(message):
    random_card_major = random.choice(major_arcana)
    bot.send_sticker(message.chat.id, random_card_major)

@bot.message_handler(commands=['send_minor'])
def minor_sender(message):
    random_card_minor = random.choice(minor_arcana)
    bot.send_sticker(message.chat.id, random_card_minor)

bot.polling(none_stop=True)