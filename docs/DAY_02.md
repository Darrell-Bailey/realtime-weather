# Day 2 Notes

## Summary of Steps
- Add docker-compose file for repeatable local infrastrucutre
- Bring the stack up and do standard health checks
- Install python kafka client
- Create a topic (weather_raw) by using the Redpanda CLI
- Add producer scripts for message generation
- Run the producer and verify the messages
- Inspect messages in Kafka UI
- Add a consumer script for verification

## Issues Encountered
Encountered an issue with Kafka where the cluster was showing offline. Diagnosed this as Kafka UI not connecting because of 127.0.0.1 issues. Configure my docker-compose file with mode: dev-container, which auto-configures correctly for Docker.