article = "Adam Levine of the band Maroon 5 has been accused of having an affair after an Instagram model named Sumner Stroh posted a series of purported DMs in a TikTok video on September 19. These stunning details were revealed just one week after his wife, Behati Prinsloo, told the world that they were expecting their third child."

substitutions = {"purported" : "suggestive",
  "of the band Maroon 5" : "the adulterer",
  "accused" : "convicted",
  "stunning" : "gruesome"}

for key, value in substitutions.items():
  article = article.replace(key,value)
  print(article)
