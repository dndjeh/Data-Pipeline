# 🚇 서울시 지하철 이용 데이터 파이프라인 구축 프로젝트

**서울열린데이터광장의 API를 활용하여 지하철 역별 승하차 인원 데이터를 수집하고,  
Python, Apache Spark, MySQL, Apache Airflow를 통해 자동화된 데이터 파이프라인을 구축한 프로젝트입니다.**

---

## 📌 프로젝트 개요

- 서울시 공공 API(Open API)를 통해 지하철 이용 데이터를 수집
- Python으로 API 호출 및 데이터 전처리
- Spark로 대용량 데이터 병렬 처리 및 정제
- MySQL에 정제된 데이터를 저장 (RDBMS 적재)
- Airflow를 활용해 주기적인 수집 및 적재 자동화

---

## 🛠 기술 스택

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white"/>
</p>

