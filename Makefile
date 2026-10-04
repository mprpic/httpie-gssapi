.PHONY: bump-minor bump-major build

define commit-tag-push
	git add . && git commit
	git tag $$(uv version --short)
	@git show HEAD
	@read -p "Push to remote? [y/N] " confirm && [ "$$confirm" = "y" ] && git push --follow-tags || echo "Skipped push."
endef

bump-minor:
	uv version --bump minor
	$(commit-tag-push)

bump-major:
	uv version --bump major
	$(commit-tag-push)

build:
	rm -rf dist/
	uv build
