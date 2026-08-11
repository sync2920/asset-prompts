# Image storage

Image binaries in this repository are stored privately in Google Drive instead of GitHub.

## Storage location

- Google Drive UI: `My Drive/X/asset-prompts`
- rclone path: `personal-drive:X/asset-prompts`
- Local working tree: this repository root

The relative directory structure is identical locally and in Drive. For example:

```text
Local:  78-morning-coffee-window/generated-v10/01.png
Drive:  X/asset-prompts/78-morning-coffee-window/generated-v10/01.png
```

## Commands

Run these from the repository root:

```bash
# Upload new or changed local images. Does not delete files.
scripts/drive-images.sh upload

# Restore images from Drive. Does not delete files.
scripts/drive-images.sh download

# Verify that every local image has a matching Drive copy.
scripts/drive-images.sh check

# Show image counts and sizes.
scripts/drive-images.sh size-local
scripts/drive-images.sh size-remote
```

The default rclone remote can be overridden when necessary:

```bash
X_IMAGE_REMOTE='another-remote:path' scripts/drive-images.sh download
```

## Safety

The helper intentionally uses `rclone copy`, not `rclone sync`, so extra files are never deleted automatically. Temporary delivery directories are excluded. Images remain in the local working tree but are ignored by Git.

The Drive folder is private unless its sharing settings are changed manually.
