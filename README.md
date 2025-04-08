# Schema Registry

Kafka 메시지용 Avro 스키마들을 저장하고 관리하는 레포지토리입니다.

## 스키마 위치
- 모든 스키마 파일은 `schemas/` 폴더에 위치합니다.

## 테스트 및 자동 등록
- `.github/workflows/register-schema.yml`에서 Kafka Schema Registry 서버로 자동 등록 설정 가능

## 사용 예시
이 스키마는 `shared-lib-avro`를 통해 Java 프로젝트에서 클래스로 사용됩니다.