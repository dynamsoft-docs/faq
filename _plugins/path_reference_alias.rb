module Jekyll
  class PathReferenceAliasPage < Page
    def initialize(site, source_dir, source_name, alias_dir)
      @site = site
      @base = site.source
      @dir = alias_dir
      @name = source_name

      process(@name)
      read_yaml(File.join(@base, source_dir), @name)
    end
  end

  class PathReferenceAliasGenerator < Generator
    safe true
    priority :low

    def generate(site)
      placeholder_files = detect_placeholders(site)
      return if placeholder_files.empty?

      placeholder_paths = placeholder_files.map { |item| item[:relative_path] }
      site.static_files.reject! { |file| placeholder_paths.include?(file.relative_path) }

      placeholder_files.each do |item|
        create_alias_pages(site, item)
      end
    end

    private

    def detect_placeholders(site)
      site.static_files.filter_map do |file|
        next unless File.extname(file.relative_path).empty?

        file_path = File.join(site.source, file.relative_path)
        next unless File.file?(file_path)

        raw = File.read(file_path, encoding: 'UTF-8').strip
        next if raw.empty?
        next unless raw.start_with?('./', '../')

        placeholder_dir = File.dirname(file.relative_path)
        target_dir = File.expand_path(raw, File.join(site.source, placeholder_dir))
        source_root = File.expand_path(site.source)

        next unless target_dir.start_with?(source_root + File::SEPARATOR)
        next unless Dir.exist?(target_dir)

        {
          relative_path: file.relative_path,
          placeholder_dir: placeholder_dir,
          placeholder_name: File.basename(file.relative_path),
          target_dir: target_dir
        }
      end
    end

    def create_alias_pages(site, placeholder)
      alias_root = File.join(placeholder[:placeholder_dir], placeholder[:placeholder_name]).tr('\\', '/')
      source_root = File.expand_path(site.source)

      Dir.glob(File.join(placeholder[:target_dir], '**', '*.md')).sort.each do |source_file|
        source_dir = File.dirname(source_file)
        source_name = File.basename(source_file)

        source_rel_dir = source_dir.sub(/^#{Regexp.escape(source_root)}[\\\/]?/, '').tr('\\', '/')
        alias_rel_dir = source_rel_dir.sub(/^#{Regexp.escape(placeholder[:target_dir].sub(/^#{Regexp.escape(source_root)}[\\\/]?/, '').tr('\\', '/'))}/, '').sub(%r{^/}, '')

        alias_dir = alias_root
        alias_dir = File.join(alias_root, alias_rel_dir).tr('\\', '/') unless alias_rel_dir.empty?

        site.pages << PathReferenceAliasPage.new(site, source_rel_dir, source_name, alias_dir)
      end
    end
  end
end
