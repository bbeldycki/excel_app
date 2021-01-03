This is still WORK IN PROGRESS.
-

This is my first web app. The purpose of this app is to process one/multiple
excel files. The web app is currently deployed on pythonanywhere:
https://flippy9004.pythonanywhere.com/.

For now, there are two built-in functionalities.

1. Column remover
2. Excel files merger


Column remover:
-  
This functionality takes two files (txt file and xlsx file). Then, the script reads all column
headers form txt file and removes columns from xlsx file with headers that do not match the ones
in txt file. The script works only for the first sheet in xlsx file and ignores the rest.

Excel files merger
-
This functionality takes multiple xlsx files and merges them into one file. Corresponding worksheets
are merged together between the excel files. For now, script works only for a specific xlsx file layout. 

Planed Functionality
-
1. Improve the messages and page layouts.
2. Implement general purpose excel files merger.
3. Implement xml files merger.
4. Review the column remover functionality for possible upgrades.

