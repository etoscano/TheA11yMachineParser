# TheA11yMachineParser

This Parser takes as input the csv output of [TheA11yMachine project](https://github.com/liip/TheA11yMachine/), obtained using the following settings
```
./a11ym  --report csv --error-level error --maximum-urls 1000  https://www.zegna.com > output.csv
```
Workers cannot be used in TheA11yMachine because the output file loses track of what URL is being analysed.

The data obtained is VERBOSE but it contains info about the page that is currently being analyzed.
This parser cleans up the data to obtain a csv that contains just the accessibility issues and the indication of the page analyzed.

![Input data](imgs/input.png)


In order to import the parsed file into Excel:

## Step 1
Go to the Data tab and click on Get External Data (not available on Excel online).

![Import data from external source in Excel](imgs/step_1.png)

## Step 2
Select "Delimited" and click Next

![Select data delimiter](imgs/step_2.png)

## Step 3
Select only "Comma" and clcik Next

![Select comma as data delimiter](imgs/step_3.png)

## Preview

Here is the data imported in Excel.

![Excel file with raw data from TheA11yMachine](imgs/raw.png)

Here is the parsed data that has been formatted in Excel.
If you wish to import data in a formatted sheet, you should import data in a DIFFERENT sheet and then copy/paste it in the formatted sheet.

![Excel file with formatted data from TheA11yMachine](imgs/formatted.png)