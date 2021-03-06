#### 문제 링크
https://www.acmicpc.net/problem/10250

<br>


## 시사점

1. 해당 문제는 호텔의 방의 수가 손님의 수보다 많으므로 사실 
방이 층 수의 방이 몇개인지는 확인할 필요가 없었다.


2. 중간에 0이 존재하는데 반복문을 써서 하나하나 더할까 생각했었는데, 시간초과가 나올 것 같아서, 어떻게 표현할까 생각을 해봤는데, 층에다가 100을 곱하고 나머지 호수를 더하는 방식을 택했습니다.

<br>

## 함수 리스트 및 설명

1. 바로 구현에 들어가서 따로 로컬 함수를 만들지는 않았습니다.

<br>


##  소스 코드 (C++) 


``` c++
/******
 * Author      :    Jiung
 * Filename    :    10250.cpp
 * Version     :    Apple clang version 12.0.0 (clang-1200.0.32.27)
 * Date        :    2021-02-22
 * Copyright   :    Free
 */
  
#include <iostream>
  
using namespace std;
  
int main() {
// 변수 입력 받기 위한 설정
    int N, h, w, s, ans;
    cin >> N;

    for(int i=0; i<N; i++) {

    // 입력 받기
        ans = 100;
        cin >> h >> w >> s;
        
        /* 구현 s % h == 0 일 경우 따로 1을 더해줄 필요가 없어서
         * 따로 두분류로 나누어 설정해봤습니다.
         */
        if(s % h == 0) {
            ans = ans * h + (s / h);
            cout << ans << endl;
        } else {
        
            ans = ans * (s % h) + (s / h);
            cout << ans+1 << endl;
        }
    }
}
```



## 코드리뷰
```
작성자 : Thedume
작성일자 2021/02/23

1.자릿수에 신경을 써야 할 문제에서는 cout보다는 printf함수를 쓰는 것이 좋아 보입니다! 
층수와 방번호를 나눠서 printf("%d%02d") 를 이용할 수 있죠
2.나머지가 0인 경우와 아닌 경우를 나눠서 연산 할 수 도 있지만
층수는 (N-1)%H+1 , 방 번호는  (N-1)/H+1 으로도 표현 할 수 있습니다!
그럼 조건문을 쓰지 않아도 될것입니다!
```

