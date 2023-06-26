# ***Web survey*** - aplikacja w postaci ankiety z analizą danych

***Temat projektu:*** 
Ocena gotowości społecznej na systemy automatycznie rozpoznające emocje - co obecnie potrafią takie systemy? </br>
Jak respondenci ocenialiby instalację 24h systemów monitoringu osób z zaburzeniami emocjonalnymi w ich miejscach zamieszkania?
******************

*Projekt łączony z przedmiotów "Rozwój Aplikacji Internetowych w Medycynie" oraz "Hurtownie i Eksploracja Danych" na studiach Inżynieria Biomedyczna, specjalizacja: Informatyka w Medycynie.*

Treść ankiety została utworzona przy użyciu materiałów z przedmiotu "Hurtownie i Eksploracja Danych" oraz korzystając z badania NASK na temat opinii internautów w temacie sztucznej inteligencji w społeczeństwie i gospodarce ([link pobierający raport z badania](https://www.nask.pl/download/30/2602/RAPORTAIONLINEs.pdf)).
W repozytorium zamieszczono kod aplikacji webowej oraz pliki *.ipynb* z kodem do analizy otrzymanych danych (w oddzielnym folderze). 

W ramach projektu wykonano:
* aplikację webową w frameworku Flask, hostowaną na stronie [Python Anywhere](https://pythonanywhere.com)
  * wykorzystane technologie: *Flask*, *SQLite*
* analizę danych otrzymanych w ankiecie w środowisku Jupyter Notebook
  * wykorzystane biblioteki: *numpy*, *pandas*, *scikit-learn*, *matplotlib*, *seaborn* oraz *apyori* ([dokumentacja biblioteki](https://pypi.org/project/apyori/))
 
___TO DO:___
* dodanie prostego i przejrzystego front-endu - ładnego :)
* użycie lepszych metod analitycznych dla danego datasetu
* ciekawsza forma prezentacji danych
* przeprowadzenia badania ponownie na innej grupie osób (bardziej zróżnicowanej wiekowo, wykształceniem, miejscem zamieszkania)
* dodanie opisu pliku *readme.md* w języku angielskim 
