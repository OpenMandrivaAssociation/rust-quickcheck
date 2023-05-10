%bcond_without check
%global debug_package %{nil}

%global crate quickcheck

Name:           rust-quickcheck
Version:        1.0.3
Release:        3
Summary:        Automatic property based testing with shrinking

# Upstream license specification: Unlicense/MIT
License:        Unlicense OR MIT
URL:            https://crates.io/crates/quickcheck
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging >= 21
BuildRequires:  (crate(env_logger) >= 0.8.2 with crate(env_logger) < 0.9.0~)
BuildRequires:  (crate(env_logger/regex) >= 0.8.2 with crate(env_logger/regex) < 0.9.0~)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
BuildRequires:  (crate(rand) >= 0.8.0 with crate(rand) < 0.9.0~)
BuildRequires:  (crate(rand/getrandom) >= 0.8.0 with crate(rand/getrandom) < 0.9.0~)
BuildRequires:  (crate(rand/small_rng) >= 0.8.0 with crate(rand/small_rng) < 0.9.0~)

%global _description %{expand:
Automatic property based testing with shrinking.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck) = 1.0.3
Requires:       (crate(rand) >= 0.8.0 with crate(rand) < 0.9.0~)
Requires:       (crate(rand/getrandom) >= 0.8.0 with crate(rand/getrandom) < 0.9.0~)
Requires:       (crate(rand/small_rng) >= 0.8.0 with crate(rand/small_rng) < 0.9.0~)
Requires:       cargo

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck/default) = 1.0.3
Requires:       cargo
Requires:       crate(quickcheck) = 1.0.3
Requires:       crate(quickcheck/regex) = 1.0.3
Requires:       crate(quickcheck/use_logging) = 1.0.3

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+env_logger-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck/env_logger) = 1.0.3
Requires:       (crate(env_logger) >= 0.8.2 with crate(env_logger) < 0.9.0~)
Requires:       cargo
Requires:       crate(quickcheck) = 1.0.3

%description -n %{name}+env_logger-devel %{_description}

This package contains library source intended for building other packages which
use the "env_logger" feature of the "%{crate}" crate.

%files       -n %{name}+env_logger-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck/log) = 1.0.3
Requires:       (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0~)
Requires:       cargo
Requires:       crate(quickcheck) = 1.0.3

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck/regex) = 1.0.3
Requires:       (crate(env_logger/regex) >= 0.8.2 with crate(env_logger/regex) < 0.9.0~)
Requires:       cargo
Requires:       crate(quickcheck) = 1.0.3

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+use_logging-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(quickcheck/use_logging) = 1.0.3
Requires:       cargo
Requires:       crate(quickcheck) = 1.0.3
Requires:       crate(quickcheck/env_logger) = 1.0.3
Requires:       crate(quickcheck/log) = 1.0.3

%description -n %{name}+use_logging-devel %{_description}

This package contains library source intended for building other packages which
use the "use_logging" feature of the "%{crate}" crate.

%files       -n %{name}+use_logging-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
