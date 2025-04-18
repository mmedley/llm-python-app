# llm-python-app

# Build the image
docker build -t mmedley/llm-app:v1 .
 
# Push the image
docker push mmedley/llm-app:v1

# Create a secret for your api key
kubectl create secret generic openai-secret --from-literal=api-key="your_openai_api_key"

kubectl apply -f deployment.yaml
 
Verify the deployment:
kubectl get deployments
kubectl get pods
kubectl get services

# Scale out pods with HPA
kubectl autoscale deployment llm-app --cpu-percent=50 --min=3 --max=10

kubectl get hpa

# install metrics server
```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

# view logs
```
kubectl logs <pod-name>
```

# testing
```
curl -X POST http://<external-ip>/generate \
-H "Content-Type: application/json" \
-d '{"prompt": "Explain Kubernetes in simple terms."}'
```

# output	
```
{
  "response": "Kubernetes is an open-source platform that manages containers..."
}
```

