# 🎲 Tärningsspelet 21

Ett textbaserat tärningsspel inspirerat av Blackjack där spelaren möter datorn (dealern).  
Målet är att komma så nära **21 poäng** som möjligt utan att gå över.

---

## 🕹️ **Spelregler**

1. Spelaren börjar och får välja att:
   - **(r)** Rulla tärningen (1–6)
   - **(s)** Stanna på sin nuvarande poäng
2. Får spelaren **över 21**, förlorar denne direkt.
3. När spelaren stannar tar **dealern** sin tur:
   - Dealern slår automatiskt tills den når **minst 17 poäng**.
   - Får dealern över 21, vinner spelaren.
4. Om ingen får över 21:
   - Den som är **närmast 21** vinner.
   - Vid lika poäng blir det **oavgjort**.
5. Efter varje runda visas ställningen (antal vinster för spelare, dealer och oavgjort).
6. Highscore sparas i filen `highscore.txt` och laddas in automatiskt nästa gång spelet startar.

---

## 📂 **Projektstruktur**

