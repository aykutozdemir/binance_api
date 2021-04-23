# LibreOffice Calc - Binance API Extension

This is a simple LibreOffice Calc extension that provides `BINANCEPRICE`, `BINANCEHIGHPRICE`, `BINANCELOWPRICE`,
`BINANCEVOLUME`, `BINANCEQUOTEVOLUME` functions from Binance's API.

## Install

Download the latest plugin from the [Releases page][releases]. Make sure you
grab the `BinanceApi.oxt` and not the source code downloads.

In LibreOffice, go to `Tools -> Extension Manager -> Add` and select the
`BinanceApi.oxt` file you downloaded. Restart LibreOffice when prompted.

## Usage

Simply pass your trading pair to the `BINANCEPRICE` function:

    =BINANCEPRICE("ROSEUSDT")      // Current price of ROSEUSDT
    =BINANCEHIGHPRICE("ROSEUSDT")  // Highest price of ROSEUSDT in last 24 hr
    =BINANCELOWPRICE("ROSEUSDT")   // Lowest price of ROSEUSDT in last 24 hr
    =BINANCEVOLUME("ROSEUSDT")     // Volume in last 24 hr in ROSE
    =BINANCEQUOTEVOLUME("ROSEUST") // Volume in last 24 hr in USDT

## Build

If you want to build the plugin yourself, you need to install `7zip`, `make`,
`python`, & the libreoffice-sdk.

Then you can just run `make` to generate `BinanceApi.oxt`.


## LICENSE

GPL-3.0
