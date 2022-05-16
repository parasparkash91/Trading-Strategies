from content.yahoofinanace_data import yf_data
from constants import INDEXSYMBOL
from content.csvfile import read_csvfile
from content.excel_file import read_excelfile
from content.store_sql import insert_temp_data
from content.oibuiltup import fno_fresh_longs_shorts
from content.volume_shockers import volume_shockers
from content.fibonacci import fibonacci
from content.pivot_calculator import Pivot_Point
from content.bulk_deals import get_bulk_deals_data, bulk_deals_data_download, insert_bulkdeals_data
from content.db_table import make_bulkdeals_data_table, make_blockdeals_data_table
from content.fii_dii import fii_dii
from content.price_oi_and_price_volume_scanners import price_oi_volume
from datetime import date
from constants import fo_symbol
from content.bollinger_band_support_and_resistance import bollinger_bands, bbands_support_resistance
from content.block_deals import get_block_deals_data, block_deals_data_download, insert_blockdeals_data
from content.backtesting import run_strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades
import content.sma_crossover
from content.high_low_52week import get_52wk_hi_lw


from content.delivery_perc_ranking import delivery_perc_ranking

if __name__ == '__main__':
    # TODO: 1. Fetch Historical Data for Cash from Yahoo Finance
    data = yf_data(symbol=INDEXSYMBOL.NIFTY50, start_date=None, end_date=None,progress=True)
    print(data)
    # # TODO: 2. Read Data From CSV file
    # read_csv_file = read_csvfile()
    # print(read_csv_file)
    # # TODO: 3. Read Data From Excel File
    # read_excel_file = read_excelfile()
    # print(read_excel_file)
    # # TODO: 4. Store Historical Data in SQL Server
    # insert_data = insert_temp_data()
    # print(insert_data)
    # # TODO: 5. FnO Fresh Longs/Shorts and OI Spurts
    # Oi_data = fno_fresh_longs_shorts()
    # print(Oi_data)
    # # TODO: 6. Volume Shockers
    # volume_shockers_result = volume_shockers()
    # print(volume_shockers_result)
    # # TODO: 7. Fibonacci
    # get_fibonacci_level = fibonacci()
    # print(get_fibonacci_level)
    # # TODO: 8. Pivot Point
    # pivot_level = Pivot_Point()
    # print(pivot_level)
    #
    # # TODO: 9. FII DII Activities
    # get_fii_dii_data = fii_dii()
    # print(get_fii_dii_data)
    #
    # # TODO: 10. Bulk Deals
    # # TODO: 10.1 For table creation in Database. Comment this function if table is already present in database
    # make_bulkdeals_data_table()
    # # TODO: 10.2 Use this function only for bulk deals data downloading
    # bulk_deals_data_download()
    # # TODO: 10.3 For insertion only
    # insert_bulkdeals_data()
    # # TODO: 10.4 For fetch bulk deals data from db
    # date = '2019-12-12'
    # get_bulk_deals_data(date=date)
    #
    # # TODO: 11. Block Deals
    # # TODO: 11.1 For table creation in Database. Comment this function if table is already present in database
    # make_blockdeals_data_table()
    # # TODO: 11.2 Use this function only for block deals data downloading
    # block_deals_data_download()
    # # TODO: 11.3 For insertion only
    # insert_blockdeals_data()
    # # TODO: 11.4 For fetch bulk deals data from db
    # date = '2019-12-10'
    # get_block_deals_data(date=date)
    #
    # # TODO: 12. Delivery perc
    # start_date = date(2019, 11, 1)
    # end_date = date(2019, 11, 29)
    # symbol = fo_symbol
    # delivery_perc= delivery_perc_ranking(symbol=symbol, start_date=start_date, end_date=end_date)
    # print(delivery_perc)
    #
    # # TODO: 13. Price OI and Price Volume scanners
    # price_oi_volume_scanner = price_oi_volume()
    # print(price_oi_volume_scanner)
    #
    # # TODO: 14. BBANDS
    # start_date = date(2019, 10, 1)
    # end_date = date(2019, 11, 29)
    # symbol = fo_symbol
    # bbands = bbands_support_resistance(symbol=symbol, start_date=start_date, end_date=end_date)
    # print(bbands)
    #
    # # TODO: 15. Backtesting
    # sma_20 = run_strategy(20)
    # print(sma_20)
    #
    # # TODO: 16. Optimization
    # for i in range(10, 30):
    #     run_strategy(i)
    #
    # # TODO: 17. Complete backtesting Analysis(Final portfolio value, Cumulative returns, Sharpe ratio, Max. drawdown,
    # #  Longest drawdown duration, Total trades, Profitable trades, Unprofitable trades)
    #
    # # Load the bars. This file was manually downloaded from Yahoo Finance.
    # feed = yahoofeed.Feed()
    # feed.addBarsFromCSV("PythonNew", "content/data-2019.csv")
    #
    # # Evaluate the strategy with the feed's bars.
    # myStrategy = content.sma_crossover.SMACrossOver(feed, "PythonNew", 20)
    #
    # # Attach different analyzers to a strategy before executing it.
    # retAnalyzer = returns.Returns()
    # myStrategy.attachAnalyzer(retAnalyzer)
    # sharpeRatioAnalyzer = sharpe.SharpeRatio()
    # myStrategy.attachAnalyzer(sharpeRatioAnalyzer)
    # drawDownAnalyzer = drawdown.DrawDown()
    # myStrategy.attachAnalyzer(drawDownAnalyzer)
    # tradesAnalyzer = trades.Trades()
    # myStrategy.attachAnalyzer(tradesAnalyzer)
    #
    # # Run the strategy.
    # myStrategy.run()
    #
    # print("Final portfolio value: $%.2f" % myStrategy.getResult())
    # print("Cumulative returns: %.2f %%" % (retAnalyzer.getCumulativeReturns()[-1] * 100))
    # print("Sharpe ratio: %.2f" % (sharpeRatioAnalyzer.getSharpeRatio(0.05)))
    # print("Max. drawdown: %.2f %%" % (drawDownAnalyzer.getMaxDrawDown() * 100))
    # print("Longest drawdown duration: %s" % (drawDownAnalyzer.getLongestDrawDownDuration()))
    #
    # print("")
    # print("Total trades: %d" % (tradesAnalyzer.getCount()))
    # if tradesAnalyzer.getCount() > 0:
    #     profits = tradesAnalyzer.getAll()
    #     print("Avg. profit: $%2.f" % (profits.mean()))
    #     print("Profits std. dev.: $%2.f" % (profits.std()))
    #     print("Max. profit: $%2.f" % (profits.max()))
    #     print("Min. profit: $%2.f" % (profits.min()))
    #     returns = tradesAnalyzer.getAllReturns()
    #     print("Avg. return: %2.f %%" % (returns.mean() * 100))
    #     print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
    #     print("Max. return: %2.f %%" % (returns.max() * 100))
    #     print("Min. return: %2.f %%" % (returns.min() * 100))
    #
    # print("")
    # print("Profitable trades: %d" % (tradesAnalyzer.getProfitableCount()))
    # if tradesAnalyzer.getProfitableCount() > 0:
    #     profits = tradesAnalyzer.getProfits()
    #     print("Avg. profit: $%2.f" % (profits.mean()))
    #     print("Profits std. dev.: $%2.f" % (profits.std()))
    #     print("Max. profit: $%2.f" % (profits.max()))
    #     print("Min. profit: $%2.f" % (profits.min()))
    #     returns = tradesAnalyzer.getPositiveReturns()
    #     print("Avg. return: %2.f %%" % (returns.mean() * 100))
    #     print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
    #     print("Max. return: %2.f %%" % (returns.max() * 100))
    #     print("Min. return: %2.f %%" % (returns.min() * 100))
    #
    # print("")
    # print("Unprofitable trades: %d" % (tradesAnalyzer.getUnprofitableCount()))
    # if tradesAnalyzer.getUnprofitableCount() > 0:
    #     losses = tradesAnalyzer.getLosses()
    #     print("Avg. loss: $%2.f" % (losses.mean()))
    #     print("Losses std. dev.: $%2.f" % (losses.std()))
    #     print("Max. loss: $%2.f" % (losses.min()))
    #     print("Min. loss: $%2.f" % (losses.max()))
    #     returns = tradesAnalyzer.getNegativeReturns()
    #     print("Avg. return: %2.f %%" % (returns.mean() * 100))
    #     print("Returns std. dev.: %2.f %%" % (returns.std() * 100))
    #     print("Max. return: %2.f %%" % (returns.max() * 100))
    #     print("Min. return: %2.f %%" % (returns.min() * 100))
    #
    # # TODO: 18. 52 Week High and 52 Week Low
    # start_date = date(2019, 1, 1)
    # end_date = date(2019, 11, 29)
    # symbol = fo_symbol
    # get_52wk_hi_lw(symbol=symbol, start_date=start_date, end_date=end_date)
