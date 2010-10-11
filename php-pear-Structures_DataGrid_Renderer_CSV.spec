%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_DataGrid_Renderer_CSV
%define		subver	dev1
%define		rel		1
Summary:	%{_pearname} - renderer driver that generates a CSV string
Summary(pl.UTF-8):	%{_pearname} - sterownik renderera do generowania ciągu znaków CSV
Name:		php-pear-%{_pearname}
Version:	0.1.5
Release:	0.%{subver}.%{rel}
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	131ecc2591cf06c56763e06015373761
URL:		http://pear.php.net/package/Structures_DataGrid_Renderer_CSV/
BuildRequires:	php-pear-PEAR >= 1:1.4.9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Renderer driver for Structures_DataGrid that generates a CSV
string.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik renderera do generowania ciągu znaków
CSV dla Structures_DataGrid.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Structures/DataGrid/Renderer/CSV.php
