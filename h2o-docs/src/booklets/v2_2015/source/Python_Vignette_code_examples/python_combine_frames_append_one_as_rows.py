In [98]: df8 = h2o.H2OFrame.from_python(np.random.randn(100,4).tolist(), column_names=list('ABCD'))

Parse Progress: [###############################] 100%
Uploaded py9607f2cc-087a-4d99-ba9f-917ca852c1f2 into cluster with 100 rows and 4 cols

In [99]: df9 = h2o.H2OFrame.from_python(
            np.random.randn(100,4).tolist(), 
            column_names=list('ABCD'))

Parse Progress: [###############################] 100%
Uploaded pycb8b3aba-77d6-4383-88dd-4729f1f2c314 into cluster with 100 rows and 4 cols

In [100]: df8.rbind(df9)
Out[100]: H2OFrame with 200 rows and 4 columns:
          A         B         C         D
0 -0.095807  0.944757  0.160959  0.271681
1 -0.950010  0.669040  0.664983  1.535805
2  0.172176  0.657167  0.970337 -0.419208
3  0.589829 -0.516749 -1.598524 -1.346773
4  1.044948 -0.281243 -0.411052  0.959717
5  0.498329  0.170340  0.124479 -0.170742
6  1.422841 -0.409794 -0.525356  2.155962
7  0.944803  1.192007 -1.075689  0.017082
8 -0.539276  0.777582 -1.090965 -2.237239
9  0.346192 -0.456974 -1.220243 -0.456305