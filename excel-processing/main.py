import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r'./test_wx.xlsx';
    df = pd.read_excel(path)
    #print(df)
    #删除微信无用列
    df = df.drop(labels='银行外部渠道交易流水号', axis=1)
    df = df.drop(labels='交易设备号', axis=1)
    df = df.drop(labels='交易地点纬度', axis=1)
    df = df.drop(labels='交易地点经度', axis=1)
    df = df.drop(labels='MAC地址', axis=1)
    df = df.drop(labels='交易支付设备IP', axis=1)
    df = df.drop(labels='交易设备类型',axis=1)
    df = df.drop(labels='消费POS机编号', axis=1)
    df = df.drop(labels='币种', axis=1)
    df = df.drop(labels='支付类型', axis=1)

    df = df.drop(labels='收款银行卡银行名称', axis=1)
    df = df.drop(labels='付款银行卡银行名称', axis=1)
    df = df.drop(labels='交易流水号', axis=1)
    df = df.drop(labels='序号', axis=1)
    df[['交易时间']] = df[['交易时间']].astype(str)
    #print(df.dtypes) #每列的类型
    #df['交易时间'] = df['交易时间'].map(lambda date: date[0:4]+"年"+ date[4:6]+"月"+ date[6:8]+"日"+ date[8:10]+"时"+ date[10:12]+"分"+ date[12:14]+"秒")
    #print(len(df['交易时间'][0])) #或print(len(df[['交易时间'][0]][0]))
    #print(df['交易时间'][0])
    df.to_excel('re_wx.xlsx')

    path = r'./test_zfb.xlsx'
    df_zfb = pd.read_excel(path)
    df_zfb = df_zfb.drop(labels='银行外部渠道交易流水号', axis=1)
    df_zfb = df_zfb.drop(labels='交易设备号', axis=1)
    df_zfb = df_zfb.drop(labels='交易地点纬度', axis=1)
    df_zfb = df_zfb.drop(labels='交易地点经度', axis=1)
    df_zfb = df_zfb.drop(labels='MAC地址', axis=1)
    df_zfb = df_zfb.drop(labels='IP归属地', axis=1)
    df_zfb = df_zfb.drop(labels='设备IP', axis=1)
    df_zfb = df_zfb.drop(labels='设备类型', axis=1)
    df_zfb = df_zfb.drop(labels='消费POS机编号', axis=1)
    df_zfb = df_zfb.drop(labels='币种', axis=1)
    df_zfb = df_zfb.drop(labels='支付类型', axis=1)

    df_zfb = df_zfb.drop(labels='收款方银行卡所属行', axis=1)
    df_zfb = df_zfb.drop(labels='付款方银行卡所属行', axis=1)
    #df = df.drop(labels='交易流水号', axis=1)
    df_zfb = df_zfb.drop(labels='序号', axis=1)
    df_zfb[['交易时间']] = df_zfb[['交易时间']].astype(str)
    df_zfb['借贷标志'] =  df_zfb['借贷标志'].map(lambda x: '入' if(x=='贷') else '出')
    # print(df.dtypes) #每列的类型
    df_zfb.to_excel('re_zfb.xlsx')

    df_zfb.rename(columns={'付款方支付帐号': '付款支付帐号', '付款方银行卡号': '付款银行卡号','收款方支付帐号':'收款支付帐号','收款方银行卡号':'收款银行卡号','借贷标志':'交易主体的出入账标识'},inplace=True)
    df = df.append(df_zfb)
    df.sort_values(by='交易时间', inplace=True, ascending=True)
    df['交易时间'] = df['交易时间'].map(
        lambda date: date[0:4] + "年" + date[4:6] + "月" + date[6:8] + "日" + date[8:10] + "时" + date[10:12] + "分" + date[
                                                                                                                  12:14] + "秒")
    df.to_excel('all.xlsx')