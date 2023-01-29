## Installation steps

1. repository를 clone 하세요
2. docker가 설치되어 있지 않다면 설치하세요
3. docker-compose를 설치 하세요
3. docker-compose를 이용해서 실행 하세요
    `docker-compose up -d --build`

## Architecture
![images](https://user-images.githubusercontent.com/22442843/215271595-dbd6b422-0cbb-4932-a327-7cd0dd44019d.png)

## API List

### works

| Method | Path | Description |
|:------:|:----:|:-----------:|
| GET    | /works/ | test 비동기 API |



## Commit Message Type

| Type          | Description                                      |
|:-------------:|--------------------------------------------------|
| `feat`        | 새로운 기능 추가                                  |
| `fix`         | 버그수정                                          |
| `docs`        | 문서 수정                                         |
| `style`       | 스타일 관련 기능(코드 포맷팅, 세미콜론 누락, 코드 자체의 변경이 없는 경우)|
| `refactor`    | 코드 리펙토링                 |
| `test`        | 테스트 코드, 리펙토링 테스트 코드 추가              |
| `chore   `    | 빌드 업무 수정, 패키지 매니저 수정(ex .gitignore 수정 같은 경우)    |
