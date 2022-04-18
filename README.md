

## Issue
- test_casting: 資料型態轉換
- test_annotations: 看函數輸入輸出的資料型態
- test_string_format: 字串format格式
- test_get_attributes: 列出物件有的__系列
- test_raw_string: 避免\生效，檔案路徑時使用
- test_unittest_fail: 單元測試失敗啟動
- test_dynamic_check_id: 動態插入function or method
- test_variable_memoey_comparsion: 查看變數記憶體大小

### Class __
- test_inheritance_private: private method 無法被繼承

### Class
__class__ 
__delattr__ 
__dict__ 
__getattribute__ 
__hash__ 
__init__ 
__method               
__module__ 
__new__ 
__reduce__ 
__reduce_ex__ 
__repr__ 
__setattr__ 
__str__ 
__weakref__ 
- test_show_docstring: __doc__
- test_enter_and_exit_example:  __enter__ and __exit__
- test_call_example: __call__
- test_get_attributes: __iter__
- test_annotations: __annotations__


## Outline
* def test_decorator(self):
  - 什麼樣的語言能夠用裝飾器?   函式可以作為引數傳遞的語言
* def test_efficiency(self):
  - 

* def test_try(self):
  - try, except, each, Exception, e, finally
* def test_show_number_after_point(self):
  - round
  - 顯示小數點後面幾位
* def test_mutable(self):
  - mutable
    - 可變變數形態，變數先指向一個指標，再指向數值
    - 當改變數值，指標不變，所指向的數值和該記憶體被更新
    - list, set, dictionary
    - 可以觀察數值改變前後的變數記憶體位址是否有變化，有變化就是immutable，反之mutable
  - immutable
    - 不可變變數形態，變數直接和數值綁定
    - 當改變數值，數值和記憶體會同時被更新
    - 舊記憶體就失去變數指定，系統會觀察若有記憶體太久沒被變數指定，就會被回收
* def test_nonlocal(self):
  - global 在local scope，調用全域變數
  - nonlocal 在local scope，調用上一層區域變數
  - 在inner function中，如果沒有改變變數，呼叫的就是上一層區域變數，此觀念與可變/不可變變數相同
* def test_thread_simple(self):
  - 全域性直譯器鎖（GIL）
* def test_thread_unsafe_object(self):
  - thread unsafe, thread同時更新同一個記憶體資料，導致資料錯誤

* def test_casting(self):
  - 更新資料型態

* def test_lambda(self):
  - 匿名函數 定義一個沒有名稱函數
  - Anonymous Function
  - 可以不用想函數名稱...
  - 有人說匿名函數不能解除綁定(不了解)
  - 優點，精簡程式碼，不增加額外變數
  - 缺點，不好讀，難以重複使用和維護
  - 在函數裡面插入一個匿名函數，已獲得函數的變數數值
  - 閉包，在函數內插入一個函數，以此在該函數結束記憶體被釋放後，還能保有函數內數值的資料
* def test_closure(self):
  - 閉包
  - 優點，在函數內插入一個函數，以此在該函數結束記憶體被釋放後，還能保有函數內數值的資料
  - 缺點，記憶體不好控制，可能記憶體外洩

* def test_encapsulation(self):
  - encapsulation 封裝
  - property功能，減少API數量
* def test_dynamic_check_id(self):
  - 工廠模式？
  - 動態插入判斷函式

* def test_yield(self):  # unfinished
  - 產生器
  - 減少記憶體使用量

* def test_set(self):
  - mutable
  - inorder
* def test_tuple(self):
  - immutable
  - 相對於class和list，節省很多記憶體

* * def test_zip(self):
  - turn two lists to a dictionary
* test_args_and_kwargs(self):
  - *args
  - **kwargs
* built-in function, 內置函數