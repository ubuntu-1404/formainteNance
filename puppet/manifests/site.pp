import "node.pp"
import "base"
node default {
	$tmp=goahead
	include deployed
}
