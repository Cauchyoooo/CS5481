from datetime import datetime

import pandas as pd
from lightweight_charts import Chart
import json


def load_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        df['time'] = pd.to_datetime(df['time'], unit="s").dt.tz_localize('UTC').dt.tz_convert('US/Eastern').dt.strftime('%Y-%m-%d %H:%M:%S')
        return df

if __name__ == '__main__':
    # 加载 JSON 数据
    df_biden = load_data('data/polymarket_biden.json')
    df_harris = load_data('data/polymarket_harris.json')
    df_trump = load_data('data/polymarket_trump.json')

    # 创建图表实例
    chart = Chart(title='US Election')

    # 展示英文的日期
    chart.run_script(f'''{chart.id}.chart.applyOptions({{ localization: {{ locale: "en-US" }} }})''')

    chart.layout(background_color='white', text_color='black')
    chart.grid(vert_enabled=False, horz_enabled=False)
    chart.legend(visible=True)

    # 添加折线图序列
    line_series_harris = chart.create_line(width=3, color='rgb(53, 110, 248)', style='solid', price_label=True)
    line_series_biden = chart.create_line(width=3, color='rgb(189, 189, 189)', price_label=True)
    line_series_trump = chart.create_line(width=3, color='rgb(234, 101, 85)', price_label=True)

    # 设置数据
    line_series_harris.set(df_harris)
    line_series_biden.set(df_biden)
    line_series_trump.set(df_trump)

    # Key events
    line_series_biden.marker(time=datetime(2024, 3, 12), position='above', color='#f68410', shape='arrow_down',
                             text='Biden Nominated')

    line_series_biden.marker(time=datetime(2024, 6, 27), position='above', color='#f68410', shape='arrow_down',
                             text='Biden Debate Loss')

    line_series_trump.marker(time=datetime(2024, 7, 13), position='below', color='#f68410', shape='arrow_up',
                             text='Trump Attempt')
    line_series_trump.marker(time=datetime(2024, 7, 15), position='above', color='#f68410', shape='arrow_down',
                             text='Vance as VP')

    line_series_biden.marker(time=datetime(2024, 7, 17), position='above', color='#f68410', shape='arrow_down',
                             text='Biden COVID News')
    line_series_biden.marker(time=datetime(2024, 7, 18), position='above', color='#f68410', shape='arrow_down',
                             text='Biden Exit Talks')

    line_series_biden.marker(time=datetime(2024, 7, 21), position='below', color='#f68410', shape='arrow_up',
                             text='Biden Exits')
    line_series_harris.marker(time=datetime(2024, 7, 22), position='below', color='#f68410', shape='arrow_up',
                              text='Harris Enters Race')

    line_series_trump.marker(time=datetime(2024, 8, 15), position='below', color='#f68410', shape='arrow_up',
                             text='VP Debate Set')

    line_series_trump.marker(time=datetime(2024, 8, 23), position='above', color='#f68410', shape='arrow_down',
                             text='Kennedy Backs Trump')

    line_series_harris.marker(time=datetime(2024, 8, 22), position='below', color='#f68410', shape='arrow_up',
                              text='Harris Confirmed')

    line_series_trump.marker(time=datetime(2024, 9, 10), position='above', color='#f68410', shape='arrow_down',
                             text='Trump Debate Loss')

    line_series_trump.marker(time=datetime(2024, 9, 15), position='below', color='#f68410', shape='arrow_up',
                             text='Trump Attacked')

    line_series_trump.marker(time=datetime(2024, 10, 1), position='above', color='#f68410', shape='arrow_down',
                             text='Vance Debate Win')

    line_series_trump.marker(time=datetime(2024, 10, 20), position='above', color='#f68410', shape='arrow_down',
                             text='Trump at McD’s')

    line_series_harris.marker(time=datetime(2024, 10, 29), position='below', color='#f68410', shape='arrow_up',
                              text='Biden: Trash Voters')
    line_series_trump.marker(time=datetime(2024, 10, 30), position='above', color='#f68410', shape='arrow_down',
                             text='Trump Drives Truck')

    line_series_trump.marker(time=datetime(2024, 11, 1), position='above', color='#f68410', shape='arrow_down',
                             text='Abortion Issue')

    # 显示图表
    chart.show(block=True)
