# Dataset Profiling Report

**Dataset:** `tweet_eval`

## Dataset Information

### train

- Rows: **45615**
- Columns: **2**
- Column Names: text, label

### test

- Rows: **12284**
- Columns: **2**
- Column Names: text, label

### validation

- Rows: **2000**
- Columns: **2**
- Column Names: text, label

---

## Text Statistics

### train

- text_column: **text**
- samples: **45615**
- avg_characters: **106.93**
- median_characters: **113.0**
- min_characters: **10**
- max_characters: **200**
- 95_percentile: **141.0**
- 99_percentile: **150.0**
- avg_words: **19.24**
- min_words: **1**
- max_words: **35**

### test

- text_column: **text**
- samples: **12284**
- avg_characters: **91.35**
- median_characters: **95.0**
- min_characters: **6**
- max_characters: **141**
- 95_percentile: **135.0**
- 99_percentile: **140.0**
- avg_words: **14.86**
- min_words: **1**
- max_words: **32**

### validation

- text_column: **text**
- samples: **2000**
- avg_characters: **107.54**
- median_characters: **113.0**
- min_characters: **28**
- max_characters: **170**
- 95_percentile: **141.0**
- 99_percentile: **148.0**
- avg_words: **19.44**
- min_words: **4**
- max_words: **31**

---

## Missing Values

### train

- text: 0
- label: 0

### test

- text: 0
- label: 0

### validation

- text: 0
- label: 0

---

## Duplicate Rows

- **train** : 26
- **test** : 0
- **validation** : 0

---

## Label Distribution

### train

- 0: 7093
- 1: 20673
- 2: 17849

### test

- 0: 3972
- 1: 5937
- 2: 2375

### validation

- 0: 312
- 1: 869
- 2: 819

---

## Random Examples

### train

#### Example 1

- **text** : I forgot all about Ice Cube being in the movie First Sunday. I think I seen this shit in the theaters.
- **label** : 0

#### Example 2

- **text** : playoffs are finally set. Chardon plays warren howland in the 1st round. if we win\u002c we play the winner of kenston v. tallmadge.
- **label** : 1

#### Example 3

- **text** : Are we just going to ignore the fact that Ice Cube got his ass whoop by Ricky Smiley at the beginning of Friday After Next???
- **label** : 1

#### Example 4

- **text** : If you live in the South Orlando area\u002c be on the lookout. @user has its 6th site opening on October 30th near the Florida Mall!
- **label** : 1

#### Example 5

- **text** : First record of Colin Baker at the BBC: BBC2 serial The Roads to Freedom. Part 5 - shown 1 Nov 1970. #DoctorWho
- **label** : 1

### test

#### Example 1

- **text** : Do you think Michelle Obama wanted to smack Melania Trump for plagiarizing her convention speech? She has the arms for it.
- **label** : 1

#### Example 2

- **text** : Well that finale was one big mindfuck 😳 #Westworld
- **label** : 1

#### Example 3

- **text** : Luis Enrique: "In the first half I can't remember Celtic having a clear chance and Messi as usual was at a really high level." #fcblive
- **label** : 1

#### Example 4

- **text** : Happy Thanksgiving from a couple of bad hombres! #movember #firefighters #thanksgiving…
- **label** : 2

#### Example 5

- **text** : @user Viper. Another fucking nazi
- **label** : 0

### validation

#### Example 1

- **text** : Performing tomorrow at the Harold Washington Cultural Center with @user come support the team
- **label** : 2

#### Example 2

- **text** : @user ur terrorist is going to be hanged tomorrow Yakub. stop sending terrorist u failed nation!!
- **label** : 0

#### Example 3

- **text** : @user if you get ungrounded tomorrow go to Lauren\u2019s birthday kickback
- **label** : 1

#### Example 4

- **text** : @user  Listening to the album right now \u002c for the 20th time lol \u002c I\u2019m on Poetic Justice now
- **label** : 2

#### Example 5

- **text** : If you don't think I'm the type of person to see Magic Mike XXL alone, on a Monday night, and get a glass of wine in a solo cup, then...
- **label** : 2

