# -*- coding:utf-8 -*-
#from echarts import Echart, Legend, Pie
import echarts

chart = echarts.Echart(u'%s的微信好友性别比例', 'from WeChat')
chart.use(echarts.Pie('WeChat',
              [{'value':335, 'name':'直接访问'},
                {'value':310, 'name':'邮件营销'},
                {'value':234, 'name':'联盟广告'},
                {'value':135, 'name':'视频广告'},
                {'value':1548, 'name':'搜索引擎'}],
              radius=["50%", "70%"]))
chart.use(echarts.Legend(["male", "female", "other"]))
del chart.json["xAxis"]
del chart.json["yAxis"]
chart.plot()