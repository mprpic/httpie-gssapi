.PHONY: bump-minor bump-major build

define commit-tag-push
	git add . && git commit -s
	git tag $$(uv version --short)
	@git show HEAD
	@read -p "Push to remote? [y/N] " confirm && [ "$$confirm" = "y" ] && git push && git push origin $$(uv version --short) || echo "Skipped push."
endef

bump-minor:
	uv version --bump minor --frozen
	$(commit-tag-push)

bump-major:
	uv version --bump major --frozen
	$(commit-tag-push)

build:
	rm -rf dist/
	uv build
