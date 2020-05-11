
- 搜索的组成
    - crawler
    - parser
    - indexer
    - link analyzer
    - query processor
    - ranker
![](https://jiaozi-oss.oss-cn-hongkong.aliyuncs.com/img/20191217160544.png)
- 相关度排序模型
    - Relevance Ranking Models(相关度排序模型):can predict whether a document is relevant to the query or not, but cannot predict the degree of relevance.
    - bm25:ES中的搜索算法
    - LMIR
- 重要性排序模型
    - PageRank:Web search
    - TrustRank:好的网站很少会链接到坏的网站

### BM25算法:
- 应用:ES中的搜索算法
- 表达式:
$Score(Q,d)=\Sigma^t_{i=1}\omega_i*R(q_i,d)$,其中$w_i$表示$q_i$的权重,$R(q_i,d)$为$q_i$和$d$的相关性.$Score(Q,d)$就是每个语速$q_i$和$d$的相关性加权和.
    - $\omega_i=IDF(q_i)=log\frac{N-n(q_i)+0.5}{n(q_i)+0.5}$

    - $R(q_i,d)=\frac{f_i*(k_1+1)}{f_i+K}*\frac{qf_i*(k_2+1)}{qf_i+k_2}$
      - $K=k_1+*(1-b+b*\frac{dl}{avgdl})$ 



### L2Rank         
- 其他缺点:
  - overfitting
  - combination of these ranking models
  
- 优势:
  - 传统排序模型的输出，既包括相关性排序模型的输出f(q,d)，也包括重要性排序模型的输出。
  - 文档本身的一些特征，比如是否是Spam等。 

- ML构成:
![](https://jiaozi-oss.oss-cn-hongkong.aliyuncs.com/img/20191218143822.png)

- Learning-to-Rank:有监督学习
  - fragwork
    ![](https://jiaozi-oss.oss-cn-hongkong.aliyuncs.com/img/20191218144400.png)
  - pointwise
  - pairwise
  - listwise

- pairwise:
  - cares about the relative order between two documents. learning to rank的算法:神经网络(neural network),感知器(perceptron),boosting(Boosting),SVM(support vector machines)
  - RankBoost:和AdaBoost类似,但是AdaBoost输出是一个文件的相似排序,但是RankBoost是文件对(document pairs).RankBoost继承了AdaBoost的优势:feature selection, convergence in training, and certain generalization abilities.
  