import os

print(os.path.isfile("result.html"))



html_text = '''
            <!/DOCTYPE html>
    <html>
        <head> 
       
        <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap" rel="stylesheet">
      <style>
      * {
      font-family: 'Gowun Dodum', sans-serif;
      }
        </style>
        
        <style type=text/css>
        div{padding:1%; width: 100%;}
        div.left{float:left;width:50%;}
        div.right{float:left;width:50%;height:free;border-left:solid black;border-width:thin; line-height:150%;}
        </style>
        </head>
            
            <body>
            <h1 style ="margin-left:500px;text-align:justify">Analysis on Beijing rooms in sales</h1>
        <p style = "text-align:right"> 清华大学经济管理学院 经 01 金秀珉 </p>
        <ul type="square">       
        <p><span style="border: 5px double #DCDCDC; padding: 0.4em;font-size:x-large">Main Factors</span></p>
        <pre><div style="border:solid #A2A2A2; margin:50px;border-width:0.3px; border-radius: 3px;padding: 0.6em 1em;background: #F1F1F3;width:900px;">
grouped = data.groupby('big district name')
plt.rcParams['font.family']='Heiti TC'
plt.rcParams['font.size']=5
title_font = {'fontsize':12,
              'fontweight':'bold'}
colors = sns.color_palette('Blues',len(grouped))
plt.pie(values,startangle=90,autopct='%.1f%%',colors = colors)
plt.rc('legend',fontsize=4)
plt.title("北京二手房数量百分比",fontdict=title_font,loc='left')
plt.legend(district)
plt.show()
        </div></pre>
    <div class="left">
        <img src="percentage.png" alt="room number_percentage" width=50% align:middle margin:50px>
    </div>
    
    <div style="float:left;width:45%;height:250;border-left:solid black;border-width:thin; line-height:150%;"> 
    <p style="margin:30px; text-align:justify;"> 朝阳 has the largest number of rooms in sales, 
        accounting for 24.1%. 
        I described this distribution using pie graph and the color gradient, 
        the more rooms, the deeper color, emphasizing the proportion. 
        海淀, where Tsinghua University is located, occupied 8.7%, 
        and ranked 5th among 17 districts in Beijing.
        What is prominent in Beijing's room distribution, 朝阳， 丰台， 通州， 大兴， 
        this four districts already occupy over 50% of the whole Beijing rooms in sales. 
        <a href ="https://image.baidu.com/search/detail?ct=503316480&z=0&tn=baiduimagedetail&ipn=d&cl=2&cm=1&sc=0&lm=-1&ie=gb18030&pn=3&rn=1&di=19470&ln=30&word=%B1%B1%BE%A9%B5%D8%CD%BC&os=92681954,76355518&cs=407736243,562645492&objurl=http%3A%2F%2Fimage1.wulinsoso.com%2Fpsd%2Fzcool%2F2014%2F01%2F05%2F1707205160.jpg&bdtype=0&simid=3533621993,536175691&pi=0&adpicid=0&timingneed=0&spn=0&is=0,0&fr=ala&ala=1&alatpl=normal&pos=1&oriquery=%E5%8C%97%E4%BA%AC%E5%9C%B0%E5%9B%BE">
        If you are interested in, you can check out Beijing map, you can see the size of each distrcit.
        </a>
        Those four districts are adjacent to each other, located on the East-South part of Beijing. 
        </p>
    </div>  
        </style> 
    <div class="left">
        <img src="average price.png" alt="average price" width=50% align:middle margin:50px>
    </div>

    <div style="float:left;width:45%;height:250;border-left:solid black;border-width:thin; line-height:150%;right margint:30px">
        <p style="margin:30px; text-align:justify;right margint:30px"> In terms of the average price, 西城 is the top and 东城 is the second, and the closer it is to central Beijing, the higher the price is. 
        海淀 is followed by a narrow gap with the 东城. 
        </p>
    </div>

    
            
            <hr style="border: dashed 5px gray;width:80%;">

    
            <div style=" text-align:justify; width:70%;line-height:150%;">
            <p><span style="border: 5px double #DCDCDC; padding: 0.4em;font-size:x-large; margin: 30px;">Other Factors</span></p>
           </div>
            <ul type="square">
            <li  style = "font-size:x-large">Heating</li>
    
            <div style=" text-align:justify; width:70%;line-height:150%;"> The price increases in order of heating, self-heating, and central-heating. 
            What is Particularly noticeable is that there is a big difference between having heat and not having heat. 
            This confirms that the presence or absence of heating greatly affects house prices. Analysis shows that heating is a very basic component of a house, 
            and the fact that it does not have it indicates that it is a house
             that does not even have a basic component of the house, 
             so this result is natural.</div>
             </li>
            <pre><div style="border:solid #A2A2A2; border-width:0.3px; border-radius: 3px; padding: 0.6em 1em;background: #F1F1F3;width:900px;">
aagroup = pd.DataFrame(data.groupby(['供暖方式'])['平均价格(元/平米）'].mean()).reset_index()
print(aagroup)
plt.rcParams['font.family']='Heiti TC'
plt.rcParams['font.size']=9
colors = sns.color_palette('light:b',len(grouped))
plt.bar(aagroup['供暖方式'],aagroup['平均价格(元/平米）'],color='skyblue',width=0.5,edgecolor="black",linewidth=0.5)
plt.title("供暖方式",fontdict=title_font,loc='left')
plt.ylabel("平均价格（元/平米）")
plt.xlabel("种类")

</div></pre>
            <img src="heat.png" alt="heat" width=400 align:middle margin:50px>
            <li style = "font-size:x-large">Elevator</li>
            <p style ="text-align:justify;width:70%;line-height:150%;">The presence or absence of an elevator did not make a big difference in the average price, but the rooms that have elevator formed finely higher average price than those don't have. </p>
            <pre><div style="border:solid #A2A2A2; border-width:0.3px; border-radius: 3px;padding: 0.6em 1em;background: #F1F1F3;width:900px;">
aagroup = pd.DataFrame(data.groupby(['配备电梯'])['平均价格(元/平米）'].mean()).reset_index()
print(aagroup)
x = np.arange(len(aagroup))
name = ['无','有']
plt.rcParams['font.family']='Heiti TC'
colors = sns.color_palette('light:b',len(grouped))
plt.bar(aagroup['配备电梯'],aagroup['平均价格(元/平米）'],color='pink',width=0.3,edgecolor="black",linewidth=0.5)
plt.title("电梯有无/价格",fontdict=title_font,loc='left')
plt.ylabel("平均价格（元/平米）",fontsize=9)
plt.xlabel("配备电梯",fontsize=9)
plt.xticks(x,name)
            </div></pre>
            <img src="elevator.png" alt="Elevator" width=400 align:left margin:50px>
            <li  style = "font-size:x-large"> Direction </li>
            <p style ="text-align:justify;width:70%;line-height:150%;">The site did not clearly divide the direction of the room into eight, 
            but divided it into more than 200 large numbers. 
            Furthermore, the data could not be significantly analyzed because the divided criteria were not clearly stated, 
            but this scatter plot shows more than 200 directions average price.  </p>
            <pre><div style="border:solid #A2A2A2; border-width:0.3px; border-radius: 3px;padding: 0.6em 1em;background: #F1F1F3;width:900px;">
aagroup = pd.DataFrame(data.groupby(['房屋朝向'])['平均价格(元/平米）'].mean()).reset_index()
print(aagroup)
plt.rcParams['font.family']='Heiti TC'
plt.rcParams['font.size']=4
title_font = {'fontsize':12,
              'fontweight':'bold'}
plt.title("房屋朝向",fontdict=title_font,loc='left')
colors = sns.color_palette('Blues',len(grouped))
sns.scatterplot(data=aagroup,x='平均价格(元/平米）', y='房屋朝向', alpha=0.5)
sns.scatterplot(c=colors)
plt.ylabel('房屋朝向',fontsize=9)
plt.xlabel('价格',fontsize=9)
plt.show()
            </div></pre>
            <img src="direction.png" alt="direction" width=400 align:middle margin:50px>
            
            
            <li  style = "font-size:x-large"> floor </li>
            <p style ="text-align:justify;width:70%;line-height:150%;">By slicing the data of original dataframe,
             i just extracted the information of which kind of floor the room is located.
              we can notice prominently the 地下 rooms have lower price, but 楼上 rooms have no significant difference. 
              This might give us a notice that rather than the floor, the location(district)
              of each room is more important factor on the price formation. </p>
            <pre><div style="border:solid #A2A2A2; border-width:0.3px; border-radius: 3px;padding: 0.6em 1em;background: #F1F1F3;width:900px;">
data['所在楼层']=data['所在楼层'].str[:3]
aagroup = pd.DataFrame(data.groupby(['所在楼层'])['平均价格(元/平米）'].mean()).reset_index()
aagroup = aagroup.sort_values(by = ['平均价格(元/平米）'],ascending=True)
print(aagroup)
x = np.arange(len(aagroup))
plt.rcParams['font.family']='Heiti TC'
colors = sns.color_palette('Blues',len(aagroup))
plt.bar(aagroup['所在楼层'],aagroup['平均价格(元/平米）'],color=colors,width=0.3,edgecolor="black",linewidth=0.5)
plt.title("所在楼层/价格",fontdict=title_font,loc='left')
plt.ylabel("平均价格（元/平米）",fontsize=9)
plt.xlabel("所在楼层",fontsize=9)
plt.xticks(x,aagroup['所在楼层'])
plt.show()

            </div></pre>
            <img src="floor.png" alt="floor" width=400 align:middle margin:50px>
            
            
            
            </body>
            <tail>
             <pre>
            </pre>
            <hr style="border: dashed 5px gray;width:80%;">
            <pre>
            </pre>
             <p><span style="border: 5px double #DCDCDC; padding: 0.4em;font-size:x-large">Conclusion</span></p>
             <pre><div style="border:solid #A2A2A2; border-width:0.3px; border-radius: 3px;padding: 0.6em 1em;background: #F1F1F3;width:1000px;line-height:150%;">The main factor that influences the increase of price is the district where rooms are located. 
The closer to the center of Beijing, more expensive rooms become. 
But, through analysis we can check out that there's clear preference on ground rooms（地上）rather than underground (地下）. 
Also, we can also heck that the existence of heating system is also important. 
The average price of rooms that don't have heating system is far below than the ones that have. </div></pre>
            
            
    </html>
    


'''
file = open('result.html','w',encoding='UTF-8')
file.write(html_text)
file.close()
