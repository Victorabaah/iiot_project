# edge-manifests

Copy-ready GitOps bundle for an IIoT edge application using:
- Kustomize base + overlays
- Argo CD Applications
- staging and production environments

## Edit these first
- ghcr.io/your-org/your-repo/edge-app
- https://github.com/your-org/edge-manifests.git
- edge-system
- MQTT broker/topic values
- edge node labels and tolerations

## Promotion model
CI/CD should update:
- overlays/staging/kustomization.yaml
- overlays/production/kustomization.yaml

Specifically:
images:
  - name: ghcr.io/your-org/your-repo/edge-app
    newTag: <commit-sha-or-release-tag>
