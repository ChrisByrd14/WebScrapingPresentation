# Scraping data and saving to file

This part of the presentation will use what was discussed in the [simple](simple/) directory, and elaborate on saving data to a CSV file.

```python
with open('somefile.csv', 'w') as file:
    writer = csv.DictWriter(file, sorted(my_dictionary[0].keys()))
    writer.writeheader()
    writer.writerows(my_dictionary)
```
